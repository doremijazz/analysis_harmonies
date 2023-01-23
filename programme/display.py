#### Display of results ####

from music21 import *

def write_analyse (partition, degres, chiffrage, freq_num, L_accord_anglo, tab_modulation):
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
        #print(i)
        #print(rep)
        #print(len(degres))
        if i < len(degres)-1:
            if str(degres[i]) != str(degres[i+1]) or (cpt<freq_num):
                p = ""
                for b1 in range (rep):
                    p = p  + " " + str(degres[i]) + "\n" +str(tab_modulation[i])
                    i+=1
                note.addLyric(p)
                
            else :
                note.addLyric(str(degres[i])+ "\n" +str(tab_modulation[i]))
                #print(note.expressions)
                i = i +rep
            
    #dessous_basse.show()
    cpt = 0
    #while j < len(chiffrage):
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
        if j < len(chiffrage)-1:
            if chiffrage[j] != chiffrage[j+1] or (cpt<freq_num):
                p = ""
                for b2 in range (rep2):
                     p = str(L_accord_anglo[j]) + "\n" + p + str(chiffrage[j])
                     j+=1
                note2.addLyric(p)
                    
            else :
                 note2.addLyric(str(L_accord_anglo[j]) + "\n" + str(chiffrage[j]))
                 j= j + rep2
    #dessus_basse.show()
    partition.show("mxl")
    return (partition)
