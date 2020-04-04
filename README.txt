###Overview

    Calculate the Hamming distances between input sample and 77 ATAC-seq datasets from 13 human primary blood cell types.
    Evaluate which type of hematopoietic cell is closest to an input sample	


###Requirement

bedtools (https://bedtools.readthedocs.io/en/latest/content/installation.html)
python (python 2.7.12 or higher or python 3)
python modules : numpy, pandas, statistics, scipy.cluster, scipy.spatial.distance


###Preprocessing
mapping : bwa (version 0.7.16a or higher)

sam to bam exchange & selecting aligned reads with high mapping quality : samtools (0.1.18 or higher)

remove duplicates : PICARD software (v1.119 or higher)

peak calling : MACS2 (v2.1.2 or higher)  --nomodel --nolambda --keep-dup all -p 0.01



###Input file format

Please input {samplename}.narrowPeak file, the output of MACS2


###Output

{samplename} directory is made and under the "findclosest" directory.
(i) Rank the peak results in the order of ascending p-values and acquire top 64000 peaks  => {samplename}.64000.bed
(ii) Calculate the Hamming distance between input sample and 77 ATAC-seq datasets => {samplename}.distanceresult.withtitle.txt
(iii) Clustering result => {samplename}.distanceresult.withtitle.pdf
(iv) Which cell type is closeset to the input sample => Please see {samplename}.close_cell_type.txt. Each column indicates "ranking", "cell type", "diatance".

above (i), (ii), (iii),(iv)  files are stored under findclosest/samplename directory


###Usage
sh calculate.sh {INPUTfile}


###Explanation of each file
(1) merge.pvalue2.64000.GEO.txt => 
	distance matrix between 77 ATAC-seq datasets from 13 human primary blood cell types (For the calculation, top 64000 peaks of each sample is used)

(2) Files in the findclosest/GEOdata directory => 
	For example, "Bcell_1.pvalue2.64000.bed" is produced by ranking the peak result in the order of ascending p-values and acquiring top 64000 peaks of Bcell_1 peak calling result.

(3) Files in the findclosest/addiotional  directory
	(i) samplelist.txt => 
		Sample name and its corresponding GSM number
	(ii) penaltyscore.sh => 
		Calculate penalty score. This script is only for 77 ATAC-seq datasets from 13 human primary blood cell types. 
		When using this script, the order of the input file is important. Please refer to the "pvalue2_64000_77samples.txt" in this directory.
	(iii) pvalue2_64000_77samples.txt => 
		Hamming distance matrix of 77 ATAC-seq datasets from 13 human primary blood cell types.
		In order to calculate the penalty score, please run
		sh penaltyscore.sh pvalue2_64000_77samples.txt 
	

(4) test1.narrowPeak  => A testdata. This data is from CLL sample. 
	If you run  
		sh calculate.sh test1.narrowPeak
	then, "test1" directory is made and under this directory, output files are stored.


###Contact

Azusa Tanaka :  a-tanaka at m.u-tokyo.ac.jp
