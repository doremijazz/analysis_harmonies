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
