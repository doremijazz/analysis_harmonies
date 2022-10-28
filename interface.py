from tkinter.filedialog import *
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

def action(event):
    
    freq = str(n.get())
    print("vous avez selectionner", freq)
    
    print(listeCombo.current())
    

def recup_fichier():
    return (askopenfilename(title="Choisir une partition",filetypes=[('mxl files','.mxl'),('all files','.*')]))

def init_interface (fenetre):


    text = Text(fenetre)
    photo = Image.open("/Users/ana/Desktop/logo_labri.png")
    photo = photo.resize((150, 50), Image.ANTIALIAS)
    UB = Image.open("/Users/ana/Desktop/logo_ub.png")
    UB = UB.resize((150, 50), Image.ANTIALIAS)
    UBM = Image.open("/Users/ana/Desktop/logo_ubm.png")
    UBM = UBM.resize((150, 50), Image.ANTIALIAS)
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

    
    
    return (fenetre)

def update_interface(fenetre, filepath):
    listeCombo.bind('<<ComboboxSelected>>',action)
    nom_du_fichier = Label(fenetre, text="Nom du fichier choisi : ", font="Timenewroman 12")
    nom_du_fichier.grid(row=4, column=0, columnspan=2)
    label = Label(fenetre, text=filepath, font="Timenewroman 12")
    label.grid(row=4, column=1, columnspan=2)
    print(freq)
    listeCombo.grid(row=3, column=0, columnspan=3)
    listeCombo.bind('<<ComboboxSelected>>',action)

freq = "NONE"

fenetre = Tk()
fenetre.title("Analyse")
fenetre.iconbitmap("/Users/ana/Downloads/icon2.ico")
fenetre.geometry("500x300")
init_interface (fenetre)
listeCombo = ttk.Combobox(fenetre)
n = StringVar()
listeCombo = ttk.Combobox(fenetre, textvariable = n)
listeCombo['values'] = ["croche","noire","noire_pointe","blanche"]
 
print(freq)

filepath = recup_fichier()
update_interface(fenetre, filepath)
fenetre.mainloop

