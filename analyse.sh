#!/bin/bash

echo "Hello World!"

python3.11 -m venv myenv
source myenv/bin/activate

pip3 install music21 

echo "Total Number of Arguments:" $#

echo "Argument values:" $@

cd ~/Downloads/analysis_harmonies/programme/
python main.py $@

echo "finish"
