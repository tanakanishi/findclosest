import sys
import pandas as pd
from scipy.cluster import hierarchy
import numpy as np
import scipy.spatial.distance as ssd


input=open(sys.argv[1])
output=sys.argv[2]

input = pd.read_csv(input,sep='\t')
input = input.set_index('V1')

#del input.index.name
df = ssd.squareform(input)

Z = hierarchy.linkage(df, 'ward')
np.savetxt(output, Z, delimiter="\t", fmt="%d")
