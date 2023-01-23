##### Main analysis harmonie MXL score ####

from music21 import *

import data_extraction
import harmonic_context_analysis
import harmonic_analysis
import display


def score_analysis(score_XML, freq, freq_num, nb_voices):
    
    #nb_voices = len(score_XML.part)
    score_XML = corpus.parse(score_XML)
    print("Data extraction")
    SATB_chord = data_extraction.main(score_XML, nb_voices)

    print("Analyze harmonic context")
    SATB_chord, tab_modulation = harmonic_context_analysis.main(SATB_chord, freq, freq_num)

    print("Hermonic nalysis")
    L_accord_anglo, degres, chiffrage = harmonic_analysis.main(score_XML, SATB_chord, tab_modulation)
    print(L_accord_anglo)
    print("Display harmonic analysis -> MuseScore")
    #score_analysed =
    display.write_analyse (score_XML, degres, chiffrage, freq_num, L_accord_anglo, tab_modulation)

    #score_analysed.show()

    print("END")
    return

def main(score_XML, nb_voices):
    
    freq =  'noire'
    freq_num = 1

    #lance le programme
    score_analysis(score_XML, freq, freq_num, nb_voices)

    return
