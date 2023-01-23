##### Data extraction #######

def main(score_XML, nb_voices):
    SATB_vrac = explore_score(score_XML)
    SATB_vrac = multiple_voices(SATB_vrac)
    SATB_chord = stacked_chords(SATB_vrac, nb_voices)
    #SATB_chord = supr_doublure(SATB_chord)
    return (SATB_chord)

#function that iterates through the given score and returns
#the notes for each of the voices
def explore_score(score_xml):
    s = score_xml
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

def multiple_voices(SATB_vrac):
    under_voices = []

    #calculate the number of voices for each part to detect multiple voices
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
        under_voices.append(cpt)

    #on ajoute un sous tableau pour chaque voix multiple
    for i in range (len(under_voices)):
        if under_voices[i] > 1 :
            if under_voices[i] < 3 :
                SATB_vrac.insert(i+1, [])
                under_voices.insert(i+1, 1)
            else :
                for y in range (under_voices[i]):
                    SATB_vrac.insert(i+1+y, [])
                    under_voices.insert(i+1+y, 1)
                    
    for nb_part in range (len(SATB_vrac)-1):
        k = 0
        if under_voices[nb_part]>1:
            for note in range (1,len(SATB_vrac[nb_part])) :
                if SATB_vrac[nb_part][note][0] == SATB_vrac[nb_part][note-1][0]:
                    k+= 1
                    SATB_vrac[nb_part+k].append(SATB_vrac[nb_part][note-1])
                else :
                    for x in range (1, under_voices[nb_part]):
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
                    
    return SATB_vrac
            
#reconstruct 4-part chords with a sixteenth-note time step
#chords are represented with values midi. ex : 60 -> Do4
def stacked_chords(SATB_vrac, nb_voices):
    chords = []
    for it in range (len(SATB_vrac)):
        new_voice = []
        chords.append(new_voice)
    
    nb_voice = 0
    for part_voice in SATB_vrac :
        list_note = []
        for note in part_voice :
            pas_time = int(note[1]//0.25) #1 -> quarter note
            for i in range (pas_time):
                chords[nb_voice].append(int(note[2]))
        nb_voice = nb_voice + 1
    #print(len(chords))
    #print(len(chords[0]))
    #print(len(chords[1]))
    vrac = []
    for i in range (len(chords[0])):
        chord = []
        for y in range (nb_voice):
            chord.append(chords[y][i])
        vrac.append(chord)
    print("Stacked chords")
    print(vrac)
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

