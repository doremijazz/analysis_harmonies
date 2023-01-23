#### Notes in harmony V.3 ###

from music21 import *

def cas(a, b):
    if a and b:
        id_cas = 0
    if a and b==False:
        id_cas = 1
    if a==False and b:
        id_cas = 2
    if a==False and b==False:
        id_cas = 3
    return id_cas

def contient_intervale(chord_fonda, p, p_2):
    intervales_1 = (chord_fonda[p] - chord_fonda[-1])%12
    intervales_2 = (chord_fonda[p_2] - chord_fonda[-1])%12
    return intervales_1==4 or intervales_1==3, intervales_2==7,intervales_1==7, intervales_2==10 or intervales_2==11, intervales_2==5

def contient (tab, x, occurence):
    cpt = 0
    for i in range (len(tab)):
        if tab[i]==x:
            cpt+=1
    if occurence == "sup_1":
        return cpt >= 1
    if occurence == "sup_2":
        return cpt>=2
    
    return cpt==occurence

def indice_note_etrangere(chord_fonda, chord_not, idx):
    i = (len(chord_fonda)-1)
    while i >=0:
        #print("fonda",chord_fonda[idx])
        #print("not",chord_not[i]%12)
        if (chord_not[i]%12)==chord_fonda[idx]%12:
            ##print(i)
            return (i)
        i=i-1
    return None

def indice_notes(chord_fonda):
    
    i=-2
    p = i
    while i > (len(chord_fonda))*(-1):
        if chord_fonda[-1] != chord_fonda[i]:
            p = i
            break
        i-=1

    j = p - 1
    p_2 = p
    ##print(p)
    
    while j > (len(chord_fonda))*(-1)-1:
        if chord_fonda[p] != chord_fonda[j]:
            p_2 = j
            break
        j-=1

    ##print(p_2)

    return(p, p_2)

def etat_fondamontal(chord_not):
    
    chord_fonda = []
    for i in range (len(chord_not)):
        chord_fonda.append(chord_not[i]%12)
    chord_fonda.sort(reverse=True)
    #print(chord_fonda)

    int_chord_fonda = chord_fonda
    
    cpt = 0
    idx = (len(chord_fonda))*-1
    #print("idx",idx)
    id_intrut = None

    
    tab = []
    tab_7 = []
    tab_4 = []
    past_chord_fonda = chord_fonda
    id_note_etrangere_tierce = None
    
    while cpt < len(chord_fonda):
        p, p_2 = indice_notes(chord_fonda)
        tierce, quinte, int1_7, int2_11, int2_4 = contient_intervale(chord_fonda, p, p_2)
        chord_fonda.insert(0, chord_fonda[-1]+12)
        del chord_fonda[-1]
        indice_cas = cas (tierce, quinte)
        tab.append(indice_cas)
        tab_7.append(int1_7)
        tab_4.append(int2_4)
        #print(int2_11)
        
        
        if int2_11 and past_chord_fonda[0]==chord_fonda[-1]:
            id_note_etrangere_tierce = (cpt-1)*-1
        elif int2_11 :
            #print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
            id_note_etrangere_tierce = cpt*-1
            #print(id_note_etrangere_tierce)
        
        etat = 1
        past_chord_fonda = chord_fonda
        cpt+=1
    #print(tab)
    #print(tab_7)
    #print(contient(tab, 3, "sup_2"))
    
    contient_true = None
    for t in tab_7:
        if t:
            contient_true = True
            break
        

    if contient(tab, 0, "sup_1"):
        #print("Pas de note étrangére dans l'accord")
        return None


    elif contient(tab, 2, "sup_1") and not contient(tab,1,"sup_2"):
        print("Note étrangére à la place de la tierce")
        if id_note_etrangere_tierce != None:
            #print("########################")
            id_intrut = indice_note_etrangere(int_chord_fonda, chord_not, (id_note_etrangere_tierce))
        else:
            x = 0
            while x < len(chord_fonda):
                if tab[x]==2 or (contient(tab, 3,1) and tab[x]==3):
                    #print(x+1)
                    #print((x+1)*(-1))
                    #print(int_chord_fonda)
                    id_intrut = indice_note_etrangere(int_chord_fonda, chord_not, (x+1)*(-1))
                    break
                else :
                    x+=1
   

    elif contient(tab, 1, "sup_1") and contient(tab, 3, "sup_2") and not contient(tab, 2, "sup_2") :
        print("Note étrangére à la place de la fondamantale")
        x = 0
        while x < len(chord_fonda):
            #print(tab_4)
            if tab_4[x] :
                #print("#@#@#@#@#@#@#@")
                #print(x)
                #print((x+1)*(-1))
                id_intrut = indice_note_etrangere(int_chord_fonda, chord_not, ((x+1)*(-1)) )
                break
            else :
                x+=1

    
    elif contient(tab, 1, 2) and not contient(tab,2,1):
        print("Note étrangére à la place de la quinte")
        x = 0
        while x < len(chord_fonda):
            if tab[x]==3 and tab_7[x]:
                id_intrut = indice_note_etrangere(int_chord_fonda, chord_not, (x-1))
                break
            else :
                x+=1
   

    else :
        print("Il y a deux note étrangére -> chercher si autre fondamantal puis voir si 3ce ou 5te")
        
    return id_intrut


def cherche_note_reel(SATB_chord, i, indice_intrut):
    note_reel = None
    j = i+1
    m = i+4
    while j < m :
        ##print(SATB_chord[i][indice_intrut])
        ##print(SATB_chord[j][indice_intrut])
        if SATB_chord[i][indice_intrut]!=SATB_chord[j][indice_intrut]:
            note_reel = SATB_chord[j][indice_intrut]
        j+=1
        
        
    return (note_reel)
