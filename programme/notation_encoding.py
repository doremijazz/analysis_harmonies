### Encodage musical notation ###

from music21 import *


seconde = ''
tierce = ''
quarte = ''
quinte = ''
sixte = ''
septieme = ''
neuvieme = ''
cinq_dim = ''
six_dim = ''
sept_dim = ''
neuf_dim = ''
aug = ''
diese = ''
bemol = ''
notation_baroque = [quinte, quinte , sixte, sixte, sixte + '\n' + quarte,  sixte + '\n' + quarte, septieme + '\n' + aug, sixte + '\n' + cinq_dim, aug + sixte, aug + quarte, cinq_dim, aug + sixte + '\n' + tierce, sixte + '\n' + aug + quarte, septieme, sixte + '\n' + quinte, quarte + '\n' + tierce, seconde, neuvieme + '\n' + septieme + '\n' + aug, septieme + '\n' + sixte + '\n' + cinq_dim, quinte + '\n' + aug + sixte + '\n' + quarte, tierce + '\n' + aug + quarte + '\n' + seconde, neuvieme + '\n' + septieme + '\n' + aug, sept_dim + '\n' + sixte + '\n' + cinq_dim, aug + sixte + '\n' + cinq_dim + '\n' + quarte,  aug + quarte + '\n' + tierce + '\n' + seconde, septieme + '\n' + cinq_dim, quinte + '\n' + aug + sixte, tierce + '\n' + aug + quarte, quarte + '\n' + aug + seconde, sept_dim, aug + sixte + '\n' + cinq_dim, aug + quarte + '\n' + tierce, aug + seconde]
notation_music21 = [['P5','M3'],['P5','m3'],['m6','m3'],['M6','M3'],['M6', 'P4'],['m6', 'P4'],['m7','P5','M3'],['m6','d5','m3'],['M6','P4','m3'],['M6','A4','M2'],['d5','m3'],['M6','m3'],['M6','A4'],['m7','P5','m3'],['M6','P5','M3'],['m6','P4','m3'],['M6','P4','M2'],['m7','P5','M3','M2'],['m7','m6','d5','m3'],['M6','P5','P4','m3'],['M6','A4','M3','M2'],['m7','m6','d5','m3'],['d7','m6','d5','m3'],['M6','d5','P4','m3'],['M6','A4','m3','M2'],['m7','A5','M3'],['M6','P5','m3'],['M6','A4','M3'],['m6','P4','M2'],['d7','d5','m3'],['M6','d5','m3'],['M6','A4','m3'],['M6','A4','A2']]
intervals_baroque = [seconde, tierce, quarte, quinte, sixte, septieme, neuvieme, bemol + seconde, bemol + tierce, bemol + quarte, cinq_dim, bemol + sixte, bemol + septieme, sept_dim, bemol + neuvieme, neuf_dim, diese + seconde, diese + tierce, diese + quarte, diese + quinte, diese + sixte, diese + septieme, diese + neuvieme]
intervals_m21 = ['M2', 'M3', 'P4', 'P5', 'M6', 'M7', 'M9', 'm2', 'm3', 'd4', 'd5', 'm6', 'm7', 'd7', 'm9', 'd9', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A9']


def compare(accord_analyse, accord_m21):
    for i in range (len(accord_m21)):
        if accord_analyse[i] != accord_m21[i] :
            return False
    #print('True')
    return True

def tradui_intervals_to_baroque_notation (accord_analyse):
    chord_trad = ""
    #print(len(intervals_baroque))
    #print(len(intervals_m21))
    for chord_interval in accord_analyse:
        index = intervals_m21.index(chord_interval)
        chord_trad += (intervals_baroque[index] + "\n")
        
    #print(chord_trad)
    return (chord_trad)

def notation_baroque_accord(chiffrage):
    chiffrage_traduit = []
    for a in range (len(chiffrage)) :
        #print("chiffrage = " , chiffrage[a])
        i = 0
        while i < (len(notation_music21)):
            if (len(chiffrage[a])) == (len(notation_music21[i])) and (compare(chiffrage[a], notation_music21[i])== True):
                #print('OK 2')
                #print(notation_music21[i])
                chiffrage_traduit.append(notation_baroque[i])
                break
            else :
                i +=1
                
        if ((len(chiffrage_traduit)<a+1)):
            #print("accord non conventionel")
            chiffrage_traduit.append(tradui_intervals_to_baroque_notation (chiffrage[a]))
                    
    return (chiffrage_traduit)
            
