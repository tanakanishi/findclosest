import sys
import warnings
import re
from statistics import mean, median,variance,stdev

#print ("Bcell"+"\t"+"CD4"+"\t"+"CD8"+"\t"+"CLP"+"\t"+"CMP"+"\t"+"Ery"+"\t"+"GMP"+"\t"+"HSC"+"\t"+"LMPP"+"\t"+"MEP"+"\t"+"MPP"+"\t"+"Mono"+"\t"+"NK")
peak_f = open(sys.argv[1])
count = 0

for line in peak_f:		 
	Bcell=0
	CD4=0
	CD8=0
	CLP=0
	CMP=0
	Ery=0
	GMP=0
	HSC=0
	LMPP=0
	MEP=0
	MPP=0
	Mono=0
	NK=0	
	line = line.replace('\n', '')
	line_l = re.split('\t', line)
	if count==78:
		for i in range(1,5):
			Bcell+=int(line_l[i])**2
		for i in range(5,10):
			CD4+=int(line_l[i])**2
		for i in range(10,15):
			CD8+=int(line_l[i])**2
		for i in range(15,20):
			CLP+=int(line_l[i])**2
		for i in range(20,28):
			CMP+=int(line_l[i])**2
		for i in range(28,36):
			Ery+=int(line_l[i])**2
		for i in range(36,43):
			GMP+=int(line_l[i])**2
		for i in range(43,50):
			HSC+=int(line_l[i])**2
		for i in range(50,53):
			LMPP+=int(line_l[i])**2
		for i in range(53,60):
			MEP+=int(line_l[i])**2
		for i in range(60,66):
			MPP+=int(line_l[i])**2
		for i in range(66,72):
			Mono+=int(line_l[i])**2
		for i in range(72,78):
			NK+=int(line_l[i])**2

		

		mydic={"Bcell":Bcell*2/5-718816465540853,"CD4":CD4*2/6-325849239103524,"CD8":CD8*2/6-507101071404770,"CLP":CLP*2/6-530182996836306,"CMP":CMP*2/9-483193249614949,"Ery":Ery*2/9-878633753938781,"GMP":GMP*2/8-512568260475069,"HSC":HSC*2/8-416006398683665,"LMPP":LMPP*2/4-361870036317937,"MEP":MEP*2/8-469755196964302,"MPP":MPP*2/7-526760976337049,"Mono":Mono*2/7-586890081206708,"NK":NK*2/7-403063620436770}
		list2=[]
		for i in mydic.values():
			list2.append(i)
		list2.sort()

		rank=1
		for i in range(0,len(list2)):
			r=list2[i]
			key1 = [k for k, v in mydic.items() if v == r]
			print(str(rank), key1[0],mydic[key1[0]])
			rank+=1



	count += 1
