from music21 import *

import main_analysis

#récupére tous les chorals de BACH de music21
def open_midi_files ():
    list_corpus = []
    print("open_midi_files")
    corpus_bach = corpus.search('bach', 'composer')
    print(len(corpus_bach))
    for choral in corpus_bach:
        list_corpus.append(choral)
    print(list_corpus)
    return list_corpus

def normalisation_corpus(files):
    s = corpus.parse(files)
    k = s.analyze('key')
    nb_voices = len(s.parts)
    difference_k_k = 60 - k.tonic.ps
    i = interval.Interval(difference_k_k)
    print(i)
    print(s.analyze('key'))
    s = s.transpose(i)
    print(s.analyze('key'))
    return files, nb_voices

def main():
    list_corpus = open_midi_files()
    data = []
    for choral in list_corpus:
        print(choral)
        choral_normalise, nb_voices = normalisation_corpus(choral)
        choral_analysis = main_analysis.main(choral_normalise, nb_voices)
        data.append(choral_analysis)

    print(data[100:300])
    return

main()

    
