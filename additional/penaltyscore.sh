#!/bin/sh
  
INPUT=$1
 name=`basename $INPUT .txt`
python plot.py $INPUT $name.result.txt
python penaltyscore.py $name.result.txt

