from music21 import *

#fonction main
def analyse_partition(partition):
    SATB_vrac = explore_partition(partition)
    SATB_chord = empile_chords(SATB_vrac)
    (L_accord_anglo) = anglo_symbole(SATB_chord)
    print(L_accord_anglo)
    L_accord_baroque = roman_symbole(partition, SATB_chord)
    print(L_accord_baroque)
    return

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

#reconstruie les accords à 4 voix avec un pas de temps à la double
#les accords sont représenté avec les valeurs midi. ex : 60 -> Do4
def empile_chords(SATB_vrac):
    chords = [[],[],[],[]]
    nb_voice = 0
    for part_voice in SATB_vrac :
        list_note = []
        for note in part_voice :
            pas_time = int(note[1]//0.25) #1 -> une noire
            for i in range (pas_time):
                chords[nb_voice].append(int(note[2]))
        nb_voice = nb_voice + 1

    vrac = []
    for i in range (len(chords[0])):
        chord = []
        for y in range (4):
            chord.append(chords[y][i])
        vrac.append(chord)
    print("Accord empilé")
    
    return vrac

#a partie des accords en valeurs midi retourne
#les symboles anglosaxon des accords
def anglo_symbole(SATB_chord):
    L = []
    fonda = []
    for one_chord in SATB_chord:
        c = chord.Chord(one_chord)
        basses = note.Note()
        basses.pitch.ps = round(one_chord[3])
        pitch.Pitch(ps=one_chord[3])
        basses.step
        
        c.duration.type = 'whole'
        cClosed = c.closedPosition()

        if basses.name != c.root().name :
            anglo = cClosed.root().name + '/' + basses.name
        else:
            anglo = cClosed.root().name
            
        
        
        symbole = harmony.chordSymbolFigureFromChord(c, True)
        if symbole[0] == 'Chord Symbol Cannot Be Identified':
            L.append(anglo)
        else:
            L.append(symbole[0])
    return (L)

#a partir des accords en valeurs midi retourne
#le chiffrage baroque des accords avec dégrés et qualification
def roman_symbole(partition, SATB_chord):
    L2 = []
    
    a = partition.analyze('key')
    a = a.parallel.tonicPitchNameWithCase
    print ('tonalité : ' , partition.analyze('key'))
    
    for anglo in SATB_chord:
        baroque = (roman.romanNumeralFromChord(chord.Chord(anglo),a))
        L2.append(baroque.figure)
    return L2
    
#partition issus du corpus de music21
#il est possible de fournir un choral à 4 voix
#au format xml issus de music21 ou d'une autre sources
partition = corpus.parse('bach/bwv108.6.xml')

#lance le programme
analyse_partition(partition)
