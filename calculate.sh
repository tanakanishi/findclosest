filename=$1

# echo ${filename}
 name=`basename $filename .narrowPeak`

if [ ! -d ./${name} ]; then mkdir ./${name}; fi
echo "calculating distances"
 sort -k8,8nr $filename |head -64000 > ./${name}/$name.64000.bed

ls -1 ./GEOdata/*.bed > ./${name}/list.$name.64000.txt

echo ./${name}/$name.64000.bed >> ./${name}/list.$name.64000.txt

sh readfile1.sh ./${name}/$name.64000.bed ./${name}/list.$name.64000.txt > ./${name}/$name.distanceresult.txt

cat ./${name}/$name.distanceresult.txt | python -c "import sys; print('\n'.join('\t'.join(c) for c in zip(*(l.split() for l in sys.stdin.readlines() if l.strip()))))" > ./${name}/trial.txt

sed -e '$d' ./${name}/$name.distanceresult.txt > ./${name}/trial2.txt
paste merge.pvalue2.64000.GEO.txt ./${name}/trial2.txt > ./${name}/tmp.txt
cat ./${name}/tmp.txt ./${name}/trial.txt > ./${name}/tmp2.txt
cat rowname.txt ./${name}/tmp2.txt  > ./${name}/tmp3.txt
paste colname.txt ./${name}/tmp3.txt > ./${name}/$name.distanceresult.withtitle.txt

rm ./${name}/tmp*.txt
rm ./${name}/trial*.txt

echo "making dendrogram"
python ColoredClustering.py ./${name}/$name.distanceresult.withtitle.txt ./${name}/$name.distanceresult.withtitle.pdf


python ward_closest.py  ./${name}/$name.distanceresult.withtitle.txt > ./${name}/$name.close_cell_type.txt

echo "finish"
