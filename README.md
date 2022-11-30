# analysis_harmonies
Analyse harmonique d'oeuvre à plusieurs voix : de la partition pour piano a une partition d'orchestre de chambre en passant par des chorals SATB.

Méthode pour utiliser le programme quand on à pas de connaissance en informatique :
------------------------------------------

UNE IMAGE DISQUE .DMG UTILISABLE SUR MAC SERA BIENTOT DISPONIBLE AINSI QUE DANS UN SEGOND TEMPS UN EXECUTABLE .EXE POUR WINDOWS

Methode pour utiliser le code :
------------------------------------------
Prés requis :

Il vous faudra tout d'abord installer music21. 
Sur Mac on peut directement taper la commande suivante dans le terminal:

sudo pip3 install music21

Pour mettre à jour, on peut taper : 

sudo pip3 install –upgrade music21

- - - - - - - - - - - - - - - - - - - - - - - 

Est pour l'utiliser il nous suffit comme cela a été fait dans ce programme de l'importer.
Dans le fichier .py il suffit donc de taper :

from music21 import *

---------------------------------------------
Télécharger le programme :

À partir de Github télécharger le fichier .zip.
Ou taper dans le terminal : git clone https://github.com/doremijazz/analysis_harmonies.git

---------------------------------------------

Utilisation du programme :

Vous pouvez lancer le programme directement dans un IDE tel que IDLE ou dans à l'aide du terminal.

Dans un IDE il suffit de faire run tout simplement. 
Pour changer le morceau à analyser il suffit de modifier la ligne -> partition = corpus.parse('bach/bwv108.6.xml').

Vous pouvez choisir une autre œuvre proposer dans le corpus de Music21 ou indiquer le chemin d'un fichier au format xml que vous souhaitez analyser (attention ce programme d'analyse des œuvres à 4 voix pour choeur seulement pour le moment).

--------------------------------------------

Vous n'avez plus qu'à analyser plein de choral et travailler vos compétences d'analyse musicale.
