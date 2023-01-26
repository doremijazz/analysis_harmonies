# analysis_harmonies
Analyse harmonique d'oeuvre à plusieurs voix : de la partition pour piano a une partition d'orchestre de chambre en passant par des chorals SATB.

Méthode pour utiliser pour la 1er fois le programme sur windows :
------------------------------------------

1. Dans un premier temps telecharger et installer [Python 3.11.1](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe "Python 3.11.1")

2. Dans un deuxiéme temps telecharger et installer [MuseScore 3.6](https://ftp.osuosl.org/pub/musescore-nightlies/windows/3x/stable/MuseScore-3.6.2.548021803-x86.paf.exe "MuseScore 3.6")

3. Dans un troisiéme temps telecharger ce repertoire Github [analysis_harmonies](https://github.com/doremijazz/analysis_harmonies/archive/refs/heads/main.zip "Analysis harmonie") et extraire le fichier.zip

3. Dans un quatrieme temps ouvrer le terminal. Pour cela vous pouvez Taper dans "Taper ici pour chercher" en bas a gauche de votre écran à coté
du symbole winwods "shell" et cliquer sur "invite de commande"

4. Et enfin copier coller les lignes de commande si dessous dans l'"invite de commande" :

``curl https://bootstrap.pypa.io/get-pip.py | python3``

``pip3 install music21``

``pip3 install tk``

``cd Downloads``

``cd Downloads/analysis_harmonies-main/analysis_harmonies-main/programme``

``python3 main.py``

Utiliser à nouveau sur Windows
-----------------------------------------

Une fois la méthode précédent réaliser à la 1er utilisation, il suffira de saisir les derniere ligne de code dans le terminal :

``cd Downloads/analysis_harmonies-main/analysis_harmonies-main/programme``

``python3 main.py``

Methode pour utiliser pour la 1er fois le code sur Mac :
------------------------------------------
1. Dans un premier temps telecharger et installer [Python 3.11.1](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe "Python 3.11.1")

2. Dans un deuxiéme temps telecharger et installer [MuseScore 3.6](https://ftp.osuosl.org/pub/musescore-nightlies/windows/3x/stable/MuseScore-3.6.2.548021803-x86.paf.exe "MuseScore 3.6")

3. Dans un quatrieme temps ouvrer le terminal et copier coller les lignes suivantes :

``curl https://bootstrap.pypa.io/get-pip.py | python3``

``pip3 install music21``

`` pip3 install python3-tk ``

``cd ~/Downloads/``

``git clone https://github.com/doremijazz/analysis_harmonies.git``

``python3 ~/Downloads/analysis_harmonies-main/analysis_harmonies-main/programme/main.py``

Utiliser à nouveau sur Mac
-----------------------------------------
Une fois la méthode précédent réaliser à la 1er utilisation, il suffira de saisir les derniere ligne de code dans le terminal :

``cd Downloads/analysis_harmonies-main/analysis_harmonies-main/programme``

``python3 main.py``

Utiliser l'interface pour analyser une partition
--------------------------------------------
Laissez vous guider par l'interface

1. Choisir un fichier au format Musicxml compressé dont l'extension est .mxl. Vous trouverez quelque partition pour tester le programme dans le dossier [Score_MXL_for_test](https://github.com/doremijazz/analysis_harmonies/tree/main/Score_MXL_for_test "Partition .mxl")
2. Choisir la fréquence harmonique de l'oeuvre. C'est à dire l'intervalle à laquelle les accords changes
3. Attendre l'exécution du programme
4. MuseScore s'ouvre et vous demande si vous souhaitez que la partition utilise une certaines police. Il suffit de valider
5. Vous pouvez étudier l'analyse générer pour apprendre 

Conclusion
-------------------------------------------

Vous n'avez plus qu'à analyser tout un tas d'oeuvre et travailler vos compétences d'analyse musicale.
