##### Main analysis harmonie MXL score ####
print("code de github, je vais m'exécuter)
from music21 import *
from tkinter.filedialog import *
from tkinter import *
from PIL import ImageTk, Image

import interface
import data_extraction
import harmonic_context_analysis
import harmonic_analysis
import display


def score_analysis(score_XML, freq, freq_nb_double):
    
    nb_voices = len(score_XML.parts)

    print("Data extraction")
    SATB_chord = data_extraction.main(score_XML, nb_voices)

    print("Analyze harmonic context")
    SATB_chord, tab_modulation, freq_num = harmonic_context_analysis.main(SATB_chord, freq, freq_nb_double)

    print("Hermonic nalysis")
    L_accord_anglo, degres, chiffrage = harmonic_analysis.main(score_XML, SATB_chord, tab_modulation)
    print(L_accord_anglo)
    print("Display harmonic analysis -> MuseScore")
    #score_analysed =
    display.write_analyse (score_XML, degres, chiffrage, freq_num, L_accord_anglo, tab_modulation)

    #score_analysed.show()

    print("END")
    return


def main():
    result_inte = interface.main()
    filepath, freq, freq_nb_double = result_inte
    print(freq)
    

    score_XML = converter.parse(filepath)

    #lance le programme
    score_analysis(score_XML, freq, freq_nb_double)
    return

main()
