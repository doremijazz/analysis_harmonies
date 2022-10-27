# analysis_harmonies
Analyse harmonique de choral à 4 voix

------------------------------------------
Prés requis :

Il vous faudra tout d'abord installer music21. 
Sur Mac on peut directement taper la commande suivante dans le terminal:

sudo pip3 install music21

Pour mettre à jour on peut taper : 

sudo pip3 install –upgrade music21

- - - - - - - - - - - - - - - - - - - - - - - 

Est pour l'utiliser il nous suffit comme cela à été fait dans ce programme de l'importer.
Dans le fichier .py il suffit donc de taper :

from music21 import *

---------------------------------------------
Télécharger le programme :

A partir de Github télécharger le fichier .zip.
Ou taper dans le terminal : git clone https://github.com/doremijazz/analysis_harmonies.git

---------------------------------------------

Utilisation du programme :

Vous pouvez lancer le prgramme directement dans un IDE tel que IDLE ou dans à l'aide du terminal.

Dans un IDE il suffit de faire run tout simplement. Pour changer le morceaux à analyser il suffit de modifier la 
ligne -> partition = corpus.parse('bach/bwv108.6.xml')
Vous pouvez choisir une autre oeuvre proposer dans le corpus de Music21 ou indiquer le chemin d'un fichier au format xml
que vous souhaitez analyser (attention ce pragramme analyse des oevres à 4 voix pour choeur seulement pour le moment).

--------------------------------------------

Vous n'avez plus qu'a analyser plein de choral et travailler vos compétence d'analyse musicale.
