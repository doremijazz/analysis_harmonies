from tkinter.filedialog import *
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

def recup_fichier():
    return (askopenfilename(title="Choisir une partition",filetypes=[('mxl files','.mxl'),('all files','.*')]))


def main ():

    fenetre = Tk()
    fenetre.title("Analyse")
    fenetre.iconbitmap("image/icon2.ico")
    fenetre.geometry("500x300")

    photo = Image.open("image/logo_labri.png")
    photo = photo.resize((150, 50), Image.Resampling.LANCZOS)
    UB = Image.open("image/logo_ub.png")
    UB = UB.resize((150, 50), Image.Resampling.LANCZOS)
    UBM = Image.open("image/logo_ubm.png")
    UBM = UBM.resize((150, 50), Image.Resampling.LANCZOS)
    test = ImageTk.PhotoImage(photo)
    test2 = ImageTk.PhotoImage(UB)
    test3 = ImageTk.PhotoImage(UBM) 

    label1 = Label(image=test)
    label2 = Label(image=test2)
    label3 = Label(image=test3) 
    label1.image = test
    label2.image = test2
    label3.image = test3

    
    label1.grid(row=0, column=0)
    label2.grid(row=0, column=1)
    label3.grid(row=0, column=2)

    text_fenetre = Label(fenetre, text="\n Bienvenu dans Analysis_harmonies \n Choisi un fichier au format mxl que tu souhaite analyser \n", font="Timenewroman 16 bold underline")
    text_fenetre.grid(row=2, column=0, columnspan=3)

    fenetre.update()

    filepath = recup_fichier()

    nom_du_fichier = Label(fenetre, text="Nom du fichier choisi : ", font="Timenewroman 12")
    nom_du_fichier.grid(row=3, column=0, columnspan=2)
    label = Label(fenetre, text=filepath, font="Timenewroman 12")
    label.grid(row=3, column=1, columnspan=2)

    fenetre.update()

    attent_freq = Label(fenetre, text="\n Veuillez choisir la fréquence harmonique dans le paneau déreoulant \n", font="Timenewroman 14")
    attent_freq.grid(row=4, column=0, columnspan=4)
    
    listeFreq = ('None','croche','noire','noire_pointe','blanche')
    liste_nb_double = [0, 2, 4, 6, 8]
    var = StringVar()
    listeCombo = ttk.Combobox(fenetre, values=var)
    listeCombo['values']=listeFreq
    listeCombo['state'] = 'readonly'
    listeCombo.current(0)
    print(listeCombo.current())
    listeCombo.grid(row=5, column=0, columnspan=3)

    fenetre.update()
    

    id_freq = listeCombo.current()
    while id_freq == 0 :
        
        id_freq = listeCombo.current()
        
        fenetre.update()

    return (filepath, listeFreq[id_freq], liste_nb_double[id_freq])


    
    



