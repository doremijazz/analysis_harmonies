#### Harmonic context analysis ####

from music21 import *

import data_for_modulation_analysis
import notes_in_harmony_3

def main(SATB_chord, freq, freq_num):

    #print(SATB_chord)
    
    #a continuer pour les notes étrangére -> corriger les None 
    SATB_chord = foreign_notes(SATB_chord, freq_num)
    #print(SATB_chord)
    
    SATB_chord, freq_num = harmonic_frequency(SATB_chord, freq)
    
    
    tab_modulation = modulation_analysis (SATB_chord)

    
    #tab_modulation = harmonic_frequency(tab_modulation, freq)

    print(SATB_chord)
    print(tab_modulation)

    return (SATB_chord, tab_modulation, freq_num)

def foreign_notes(SATB_chord, freq_num):
    i = 0
    while i < (len(SATB_chord)):
        print("initchord", SATB_chord[i])
        while SATB_chord[i][0]==0 and SATB_chord[i][1]==0 and SATB_chord[i][2]==0:
            i = i+1
        #print('init')
        indice_intrut = notes_in_harmony_3.etat_fondamontal(SATB_chord[i])
        #print(indice_intrut)
        if indice_intrut != None:        
            note_reel = notes_in_harmony_3.cherche_note_reel(SATB_chord, i, indice_intrut)
            print("note reel", note_reel)
            if note_reel != None:
                SATB_chord[i][indice_intrut] = note_reel
                print("newchord",SATB_chord[i])
        if ((i + (freq_num*4))%freq_num) == 0:
            i = (i + (freq_num*4))
        else :
            i = ((i + (freq_num*4))//freq_num)*4
        print(i)
        
    return(SATB_chord)

def harmonic_frequency(SATB_chord, freq):
    freq_num = 1.0
    if freq == 'croche':
        freq_num = 0.5
        return (SATB_chord[0::2], freq_num)
    if freq == 'noire':
        freq_num = 1.0
        return (SATB_chord[0::4], freq_num)
    if freq == 'noire_pointe':
        freq_num = 1.5
        return (SATB_chord[0::6], freq_num)
    if freq == 'blanche':
        freq_num = 2.0
        return (SATB_chord[0::8], freq_num)
    return (SATB_chord, freq_num)

def modulation_analysis (SATB_chord) :
    
    b = data_for_modulation_analysis.write_chord(SATB_chord)
    ka = analysis.floatingKey.KeyAnalyzer(b)
    ka.windowSize = 2
    modu_by_chord = ka.run()
    modu_by_chord = data_for_modulation_analysis.pivot(modu_by_chord,SATB_chord)
  
    return(modu_by_chord)
