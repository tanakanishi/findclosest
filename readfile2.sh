#!/bin/sh




INPUT1=$1
INPUT2=$2

#name1=`basename $INPUT1 .bed`
#name2=`basename $INPUT2 .bed`



a=`subtractBed -a $INPUT1 -b $INPUT2  | python distance.py`


b=`subtractBed -a $INPUT2 -b $INPUT1  | python distance.py`


echo  $((a+b))

