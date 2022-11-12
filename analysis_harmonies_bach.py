from music21 import *
from tkinter.filedialog import *
from tkinter import *
from PIL import ImageTk, Image
global freq
global freq_num
import interface

#fonction main
def analyse_partition(partition):
    nb_voices = len(partition.parts)
    print(nb_voices)
    SATB_vrac = explore_partition(partition)
    SATB_vrac = voix_multiple(SATB_vrac)
    SATB_chord = empile_chords(SATB_vrac, nb_voices)
    #SATB_chord = supr_doublure(SATB_chord)
    SATB_chord = frequence_harmonique(SATB_chord)
    (L_accord_anglo) = anglo_symbole(SATB_chord)
    print(L_accord_anglo)
    degres, chiffrage = roman_symbole(partition, SATB_chord)
    print(degres, chiffrage)
    write_analyse (partition, degres, chiffrage)
    return

def dim(a):
    if not type(a) == list:
        return 0
    return [len(a)] + dim(a[0])

#fonction qui parcourt la partition donnée et retourne
#les notes pour chacune des voix
def explore_partition(partition):
    s = partition
    score = []
    for part in s.parts:
        voice =[]
        
        for note in part.flat.notes:
            if note.isChord:
                start = note.offset
                duration = note.quarterLength

                for chord_note in note.pitches:
                    pitch = chord_note.ps
                    voice.append([start, duration, pitch])
                    
                
            if note.isNote:
                start = note.offset
                duration = note.quarterLength
                if len(voice)>1 and (voice[-1][0] + voice[-1][1]) < start:
                    voice.append([(voice[-1][0] + voice[-1][1]), start-((voice[-1][0] + voice[-1][1])), 0.0])
                pitch = note.pitch.ps
                voice.append([start, duration, pitch])

                
        score.append(voice)
    return score

def voix_multiple(SATB_vrac):
    nb_sous_voix = []

    #on calcule le nb de voix pour chaque partie pour detecter les voix multiple
    for part_voice in SATB_vrac :
        cpt = 1
        k = 1
        for note in range (len(part_voice)-1) :
            if part_voice[note][0] == part_voice[note+1][0]:
                k += 1
            else :
                if k > cpt:
                    cpt = k
                k = 1
        nb_sous_voix.append(cpt)

    #on ajoute un sous tableau pour chaque voix multiple
    for i in range (len(nb_sous_voix)):
        if nb_sous_voix[i] > 1 :
            if nb_sous_voix[i] < 3 :
                SATB_vrac.insert(i+1, [])
                nb_sous_voix.insert(i+1, 1)
            else :
                for y in range (nb_sous_voix[i]):
                    SATB_vrac.insert(i+1+y, [])
                    nb_sous_voix.insert(i+1+y, 1)
                    
    for nb_part in range (len(SATB_vrac)-1):
        k = 0
        if nb_sous_voix[nb_part]>1:
            for note in range (1,len(SATB_vrac[nb_part])) :
                if SATB_vrac[nb_part][note][0] == SATB_vrac[nb_part][note-1][0]:
                    k+= 1
                    SATB_vrac[nb_part+k].append(SATB_vrac[nb_part][note-1])
                else :
                    for x in range (1, nb_sous_voix[nb_part]):
                        if len(SATB_vrac[nb_part+x])==0:
                            SATB_vrac[nb_part+x].append(SATB_vrac[nb_part][note-1])
                            
                        SATB_vrac[nb_part+x].append(SATB_vrac[nb_part][note])
                    k = 1
            h = len(SATB_vrac[nb_part])
            z = 1
            while z < h :
                if SATB_vrac[nb_part][z][0] == SATB_vrac[nb_part][z-1][0]:
                    del SATB_vrac[nb_part][z-1]
                    h = h - 1
                z+=1
                    
                    
    print ("len",len(SATB_vrac[0]))
    print ("len",len(SATB_vrac[1]))
    print ("len",len(SATB_vrac[2]))
    print (SATB_vrac[0])
    print (SATB_vrac[1])
    print (SATB_vrac[2])
    
    print(nb_sous_voix) 
    return SATB_vrac
            
    

#reconstruie les accords à 4 voix avec un pas de temps à la double
#les accords sont représenté avec les valeurs midi. ex : 60 -> Do4
def empile_chords(SATB_vrac, nb_voices):
    chords = []
    for it in range (len(SATB_vrac)):
        new_voice = []
        chords.append(new_voice)
    
    nb_voice = 0
    for part_voice in SATB_vrac :
        list_note = []
        for note in part_voice :
            pas_time = int(note[1]//0.25) #1 -> une noire
            for i in range (pas_time):
                chords[nb_voice].append(int(note[2]))
        nb_voice = nb_voice + 1
    print(len(chords))
    print(len(chords[0]))
    print(len(chords[1]))
    vrac = []
    for i in range (len(chords[0])):
        chord = []
        for y in range (nb_voice):
            chord.append(chords[y][i])
        vrac.append(chord)
    print("Accord empilé")

    return vrac

def supr_doublure(SATB_chord):
    chord_simplifie = []
    for chord_8 in SATB_chord:
        new_list = []
        for note_chord in chord_8 :
            octave = note_chord//12
            cpt = 1
            for OC in range (1,octave) :
                octave_inf = note_chord-12*OC
                octave_sup = note_chord+12
                #and (octave_sup not in new_list)
                if (note_chord not in new_list) and (octave_inf not in chord_8) :
                    cpt = cpt+1
            if cpt == octave:
                new_list.append(note_chord)
        chord_simplifie.append(new_list)
    print(chord_simplifie)
    return (chord_simplifie)

def frequence_harmonique(SATB_chord):
    if freq == 'croche':
        freq_num = 0.5
        return (SATB_chord[0::2])
    if freq == 'noire':
        freq_num = 1.0
        return (SATB_chord[0::4])
    if freq == 'noire_pointe':
        freq_num = 1.5
        return (SATB_chord[0::6])
    if freq == 'blanche':
        freq_num = 2.0
        return (SATB_chord[0::8])
    return (SATB_chord)



#a partie des accords en valeurs midi retourne
#les symboles anglosaxon des accords
def anglo_symbole(SATB_chord):
    L = []
    fonda = []
    for one_chord in SATB_chord:
        c = chord.Chord(one_chord)
        c.closedPosition(forceOctave=4, inPlace=True)
        #c.closedPosition(forceOctave=4, inPlace=True)
        basses = note.Note()
        basses.pitch.ps = round(one_chord[len(one_chord)-1])
        pitch.Pitch(ps=one_chord[len(one_chord)-1])
        basses.step
        
        c.duration.type = 'whole'
        
        
        if basses.name != c.root().name :
            anglo = c.root().name + '/' + basses.name
        else:
            anglo = c.root().name
        print(c.quality)
        c6_again = harmony.ChordSymbol(root=c[0], bass=c.bass(), kind=c.quality)
        
        
        #c9.containsSeventh()
        #Accord. isSwissAugmentedSixth
        #Accord. isSeventhOfType
        #cChord.isNinth()
        #isItalianAugmentedSixth
        #Accord. isFrenchAugmentedSixth
        #Accord. isDiminishedSeventh
        #Accord. isAugmentedTriad
        #Accord. isAugmentedSixth
        roman.RomanNumeral('I7#5b3').figuresWritten
        
        symbole = harmony.chordSymbolFigureFromChord(c, True)
        if symbole[0] == 'Chord Symbol Cannot Be Identified':
            L.append(anglo)
            #L.append(c6_again.figure)
        else:
            #L.append(c6_again.figure)
            L.append(symbole[0])
        print("n",c6_again)
        print("s",symbole)
    return (L)

#a partir des accords en valeurs midi retourne
#le chiffrage baroque des accords avec dégrés et qualification
def roman_symbole(partition, SATB_chord):
    degres = []
    chiffrage = []
    
    a = partition.analyze('key')
    a = a.tonicPitchNameWithCase
    print(a)
    print ('tonalité : ' , partition.analyze('key'))
    
    for anglo in SATB_chord:
        c = chord.Chord(anglo)
        c.closedPosition(forceOctave=4, inPlace=True)
        degres.append((roman.romanNumeralFromChord(c, key.Key(a))).romanNumeralAlone)
        print(roman.romanNumeralFromChord(c, key.Key(a)))
        c.annotateIntervals()
        basse_chiffre = ""
        for l in c.lyrics:
            basse_chiffre = basse_chiffre + "\n" + l.text
        chiffrage.append(basse_chiffre)
    return (degres, chiffrage)

def write_analyse (partition, degres, chiffrage):
    dessous_basse = partition.parts[-1]
    dessus_basse = partition.parts[-2]

    i = 0
    j = 0
    cpt = 0
    for note in dessous_basse.flat.notes:
        duration = note.quarterLength
        rep = int(duration//freq_num)
        if cpt == 0 and rep == 0:
            rep = 1
            cpt+=duration
        elif rep == 0:
            cpt+=duration
        if cpt >= freq_num:
            cpt = 0
        print(rep)
        for b1 in range (rep):
            note.addLyric(str(degres[i]))
        i = i +rep
    dessous_basse.show()
    cpt = 0
    for note2 in dessus_basse.flat.notes:
        duration2 = note2.quarterLength
        rep2 = int(duration2//freq_num)
        
        if cpt == 0 and rep2 == 0:
            rep2 = 1
            cpt+=duration2
        elif rep2 == 0:
            cpt+=duration2
        if cpt >= freq_num:
            cpt = 0
        
    
        for b2 in range (rep2):
            note2.addLyric(str(chiffrage[j]))
        j= j + rep2
    dessus_basse.show()
    partition.show()
    return
    


#partition issus du corpus de music21
#il est possible de fournir un choral à 4 voix
#au format xml issus de music21 ou d'une autre sources
#partition = corpus.parse('bach/bwv108.6.xml')

##############################################@

#result_inte = interface.main()
#filepath, freq = result_inte
#freq =  'noire'
#freq_num = 1
#partition = converter.parse(filepath)

#lance le programme
#analyse_partition(partition)
