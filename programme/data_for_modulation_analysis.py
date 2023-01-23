#### Data for harmonic analysis ###

from music21 import *

def pivot(modu_by_chord, SATB_chord):
    for i in range (len(SATB_chord)):
        #print(i)
        if modu_by_chord[i-1] != modu_by_chord[i]:
            c1 = chord.Chord(SATB_chord[i-1])
            c2 = chord.Chord(SATB_chord[i-2])
            c1.closedPosition(forceOctave=4, inPlace=True)
            c2.closedPosition(forceOctave=4, inPlace=True)
            #print((roman.romanNumeralFromChord(c1, modu_by_chord[i])).romanNumeralAlone)
            if ((roman.romanNumeralFromChord(c2, modu_by_chord[i])).romanNumeralAlone) == 'V':
                #print('PIVOT')
                modu_by_chord[i-1] = modu_by_chord[i]
                modu_by_chord[i-2] = modu_by_chord[i]
            elif ((roman.romanNumeralFromChord(c1, modu_by_chord[i])).romanNumeralAlone) == 'V':
                #print('PIVOT')
                modu_by_chord[i-1] = modu_by_chord[i]
            
    return(modu_by_chord)

def write_chord(SATB_chord):
    partition_chord = stream.Score(id='partition_chord') 
    partie = stream.Part(id = 'partie')
    for i in range (len(SATB_chord)) :
        new_ronde = SATB_chord[i]
        mesure = stream.Measure(number = i)
        #print(new_ronde)
        mesure.append(chord.Chord(new_ronde, type="whole"))
        partie.append(mesure)
    partition_chord.insert(0,partie)
    partition_chord.write('midi', fp='chord_ronde')
    #print(partition_chord)
    #partition_chord.show()
    return(partition_chord)
