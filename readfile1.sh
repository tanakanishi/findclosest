#!/bin/sh

file1=$1
file2=$2
cat ${file2}| while read line2
do
 sh readfile2.sh $file1 $line2 
done


