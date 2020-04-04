import sys
import warnings
import re
import collections
from functools import reduce

def flatten_loop(l):
	i = 0
	while i < len(l):
		while isinstance(l[i], collections.Iterable):
			if not l[i]:
				l.pop(i)
				i -= 1
				break
			else:
				l[i:i + 1] = l[i]
		i += 1
	return l


data = open(sys.argv[1]) 


cells ={'Bcell':[0,1,2,3],'CD4':[4,5,6,7,8],'CD8':[9,10,11,12,13],'CLP':[14,15,16,17,18],'CMP':[19,20,21,22,23,24,25,26],'Ery':[27,28,29,30,31,32,33,34],'GMP':[35,36,37,38,39,40,41],'HSC':[42,43,44,45,46,47,48],'LMPP':[49,50,51],'MEP':[52,53,54,55,56,57,58],'MPP':[59,60,61,62,63,64],'Mono':[65,66,67,68,69,70],'NK':[71,72,73,74,75,76]}
peak_l = {}
output = {'Bcell':[],'CD4':[],'CD8':[],'CLP':[],'CMP':[],'Ery':[],'GMP':[],'HSC':[],'LMPP':[],'MEP':[],'MPP':[],'Mono':[],'NK':[]}


num_line = 76  

for line in data:
	B=0
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
	line = line.replace('\n','' )

	line_l = re.split('\t', line)
	num_line += 1


	if int(line_l[0]) <= 76 and int(line_l[1]) <= 76:

		cells[num_line]=[int(line_l[0]),int(line_l[1])]
	elif int(line_l[0]) > 76 and int(line_l[1]) <= 76:

		cells[num_line]=[cells[int(line_l[0])],int(line_l[1])]
	elif int(line_l[0]) <= 76 and int(line_l[1]) > 76:
		cells[num_line]=[cells[int(line_l[1])],int(line_l[0])]
	else:
		cells[num_line]=[cells[int(line_l[0])],cells[int(line_l[1])]]


	result=flatten_loop(cells[num_line])

	
	for i in result:

		if 0<=i<=3:
			B+=1
		if 4<=i<=8:
			CD4+=1
		if 9<=i<=13:
			CD8+=1
		if 14<=i<=18:
			CLP+=1
		if 19<=i<=26:
			CMP+=1
		if 27<=i<=34:
			Ery+=1
		if 35<=i<=41:
			GMP+=1
		if 42<=i<=48:
			HSC+=1
		if 49<=i<=51:
			LMPP+=1
		if 52<=i<=58:
			MEP+=1
		if 59<=i<=64:
			MPP+=1
		if 65<=i<=70:
			Mono+=1
		if 71<=i<=76:
			NK+=1
	


	if B==4 or CD4==5 or CD8==5 or CLP==5 or CMP==8 or Ery==8 or GMP==7 or HSC==7 or LMPP==3 or MEP==7 or MPP==6 or Mono==6 or NK==6:
		value=B+CD4+CD8+CLP+CMP+Ery+GMP+HSC+LMPP+MEP+MPP+Mono+NK

		if B==4:
			sum1=value-B
			output['Bcell'].append(int(sum1))
		if CD4==5:
			sum2=value-CD4
			output['CD4'].append(int(sum2))
		if CD8==5:
			sum3=value-CD8
			output['CD8'].append(int(sum3))
		if CLP==5:
			sum4=value-CLP
			output['CLP'].append(int(sum4))
		if CMP==8:
			sum5=value-CMP
			output['CMP'].append(int(sum5))
		if Ery==8:
			sum6=value-Ery
			output['Ery'].append(int(sum6))
		if GMP==7:
			sum7=value-GMP
			output['GMP'].append(int(sum7))
		if HSC==7:
			sum8=value-HSC
			output['HSC'].append(int(sum8))
		if LMPP==3:
			sum9=value-LMPP
			output['LMPP'].append(int(sum9))
		if MEP==7:
			sum10=value-MEP
			output['MEP'].append(int(sum10))

		if MPP==6:
			sum11=value-MPP
			output['MPP'].append(int(sum11))
		if Mono==6:
			sum12=value-Mono
			output['Mono'].append(int(sum12))
		if NK==6:
			sum13=value-NK
			output['NK'].append(int(sum13))



z=int(output['Bcell'][0])+int(output['CD4'][0])+int(output['CD8'][0])+int(output['CLP'][0])+int(output['CMP'][0])+int(output['Ery'][0])+int(output['GMP'][0])+int(output['HSC'][0])+int(output['LMPP'][0])+int(output['MEP'][0])+int(output['MPP'][0])+int(output['Mono'][0])+int(output['NK'][0])

print(str(z))
