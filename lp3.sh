#!/bin/dash
latestFile=$(ls *.py -tp | head -1)
python3 $latestFile
