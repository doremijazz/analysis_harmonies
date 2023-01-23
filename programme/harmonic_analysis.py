#### Harmonic analysis ####

from music21 import *

import notation_encoding

def main(score_XML, SATB_chord, tab_modulation):
    
    (L_accord_anglo) = anglo_symbole(SATB_chord)
    print(L_accord_anglo)
    degres, chiffrage = roman_symbole(score_XML, SATB_chord, tab_modulation)
    
    return (L_accord_anglo, degres, chiffrage)

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
        #print(c.quality)
        c6_again = harmony.ChordSymbol(root=c[0], bass=c.bass(), kind=c.quality)
        
        roman.RomanNumeral('I7#5b3').figuresWritten
        
        symbole = harmony.chordSymbolFigureFromChord(c, True)
        if symbole[0] == 'Chord Symbol Cannot Be Identified':
            L.append(anglo)
            #L.append(c6_again.figure)
        else:
            #L.append(c6_again.figure)
            L.append(symbole[0])
        #print("n",c6_again)
        #print("s",symbole)
    return (L)

#a partir des accords en valeurs midi retourne
#le chiffrage baroque des accords avec dégrés et qualification
def roman_symbole(partition, SATB_chord, tab_modulation):
    degres = []
    chiffrage = []
    i = 0

    
    for anglo in SATB_chord:
        c = chord.Chord(anglo)
        c.closedPosition(forceOctave=4, inPlace=True)
        degres.append((roman.romanNumeralFromChord(c, tab_modulation[i])).romanNumeralAlone)
        #print(tab_modulation[i])
        #print((roman.romanNumeralFromChord(c, tab_modulation[i])).romanNumeralAlone)
        if degres[-1] == "VII" or degres[-1] == "vii":
            degres[-1] = 'VII \n /V sf'
        elif degres[-1] == "III":
            degres[-1] = 'i sf'
        elif degres[-1] == "iii":
             degres[-1] = 'I sf'
        
        c3 = c.annotateIntervals(inPlace=False, stripSpecifiers=False)
        chiffrage.append([ly.text for ly in c3.lyrics])
        #print(roman.romanNumeralFromChord(c, tab_modulation[i]))
        i +=1

    #print(chiffrage)

    chiffrage = notation_encoding.notation_baroque_accord(chiffrage)
    #print(chiffrage)
       
    return (degres, chiffrage)
