#### Notes in harmony ###

from music21 import *

def contient_tierce(chord_not, cpt, tierce):
    
    
    while cpt < len(chord_not):
        intervales_1 = (chord_not[-2] - chord_not[-1])%12
        #print(chord_not)
        #print (intervales_1)
        if intervales_1!=4 and intervales_1!=3:
            #print (intervales_1)
            chord_not[0] = chord_not[0] - 12
            chord_not.insert(-1, chord_not[0])
            del chord_not[0]
            chord_not.sort(reverse=True)
            cpt+=1
        else:
            return True
            
    return False
    

def contient_quinte(chord_not, cpt, quinte):
    intervales_2 = (chord_not[-3] - chord_not[-1])%12
    if intervales_2==7:
        return True
    elif intervales_2!=7:
        if cpt == len(chord_not):
            return False
        else:
            chord_not[-1] = chord_not[-1] + 12
            chord_not.insert(0, chord_not[-1])
            del chord_not[-1]
            chord_not.sort(reverse=True)
            contient_quinte(chord_not, cpt+1, quinte)
    
    return False


def etat_fondamontal(chord_not, cpt, tierce, quinte, indice_intrut):
       
    tierce = contient_tierce(chord_not, 0, tierce)
    quinte = contient_quinte(chord_not, 0, quinte)
    #print(tierce, quinte)
        
        
    if tierce==False and quinte==False:
        #print("note etrangere dans l'accord")
        return(-1)
        
    elif tierce==True and quinte==True:
        #print("pas de note etrangére OK")
        return (None)
        
    else:
        #print("note etrangere dans l'accord")
        if tierce == False:
            return(-2)
        if quinte == False:
            return(-3)
        
    return (indice_intrut)
        


def cherche_note_reel(SATB_chord, i, indice_intrut):
    note_reel = None
    for j in range ((i+1),6):
        #print(SATB_chord[i][indice_intrut])
        #print(SATB_chord[j][indice_intrut])
        if SATB_chord[i][indice_intrut]!=SATB_chord[j][indice_intrut]:
            note_reel = SATB_chord[j][indice_intrut]
    return (note_reel)
