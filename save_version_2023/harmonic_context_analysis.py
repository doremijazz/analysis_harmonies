#### Harmonic context analysis ####

from music21 import *

import data_for_modulation_analysis
import notes_in_harmony

def main(SATB_chord, freq):
    #a continuer pour les notes étrangére -> corriger les None 
    #SATB_chord = foreign_notes(SATB_chord)
    
    tab_modulation = modulation_analysis (SATB_chord)

    SATB_chord = harmonic_frequency(SATB_chord, freq)

    return (SATB_chord, tab_modulation)

def foreign_notes(SATB_chord):
    for i in range (len(SATB_chord)):
        #print("initchord", SATB_chord[i])
        #print('init')
        indice_intrut = notes_in_harmony.etat_fondamontal(SATB_chord[i],0, True, True, None)
        #print(indice_intrut)
        if indice_intrut != None:
            note_reel = notes_in_harmony.cherche_note_reel(SATB_chord, i, indice_intrut)
            #print("note reel", note_reel)
            SATB_chord[i][indice_intrut] = note_reel
            #print("newchord",SATB_chord[i])
        
    return(SATB_chord)

def harmonic_frequency(SATB_chord, freq):
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

def modulation_analysis (SATB_chord) :
    
    b = data_for_modulation_analysis.write_chord(SATB_chord)
    ka = analysis.floatingKey.KeyAnalyzer(b)
    ka.windowSize = 2
    modu_by_chord = ka.run()
    modu_by_chord = data_for_modulation_analysis.pivot(modu_by_chord,SATB_chord)
  
    return(modu_by_chord)
