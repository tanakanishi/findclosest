import sys
import pandas as pd
import numpy as np
import copy
import scipy.spatial.distance as ssd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage


input = open(sys.argv[1])
input = pd.read_csv(input,sep='\t')
input = input.set_index('V1')

output = sys.argv[2]


X = ssd.squareform(input)
Z = linkage(X, method = "ward")
dn = dendrogram(Z) #, no_plot = True)


## setup known clustering

# label lists by hands
#label_list =  ['B', 'B', 'B', 'B', 'CD4', 'CD4', 'CD4', 'CD4', 'CD4', 'CD8', 'CD8', 'CD8', 'CD8', 'CD8', 'CLP', 'CLP', 'CLP', 'CLP', 'CLP', 'CMP', 'CMP', 'CMP', 'CMP', 'CMP', 'CMP', 'CMP', 'CMP', 'Ery', 'Ery', 'Ery', 'Ery', 'Ery', 'Ery', 'Ery', 'Ery', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'HSC', 'HSC', 'HSC', 'HSC', 'HSC', 'HSC', 'HSC', 'LMPP', 'LMPP', 'LMPP', 'MEP', 'MEP', 'MEP', 'MEP', 'MEP', 'MEP', 'MEP', 'MPP', 'MPP', 'MPP', 'MPP', 'MPP', 'MPP', 'Mono', 'Mono', 'Mono', 'Mono', 'Mono', 'Mono', 'NK', 'NK', 'NK', 'NK', 'NK', 'NK']

# make label lists from indices of tables
label_list=[]
for i in input.index:
	label_list.append(i)

# make a list of classification
classif_dict = {
    'B':[[], '#9370db'], 
    'CD4+T':[[], '#6495ed'], 
    'CD8+T':[[], '#0000cd'], 
    'CLP':[[], '#008080'], 
    'CMP':[[], '#daa520'], 
    'Ery':[[], '#800000'],
    'GMP':[[], '#f4a460'], 
    'HSC':[[], '#006400'],
    'LMPP':[[], '#00FFFF'], 
    'MEP':[[], '#FF4500'], 
    'MPP':[[], '#32cd32'], 
    'Mono':[[],'#ff69b4'],
    'NK':[[], '#800080'],
    'sample':[[], '#696969']
}

# color for mixed nodes
def RGB(red, green, blue):
    return (red/256, green/256, blue/256)

def colorcode(c):
    return RGB(int(c[1:3], 16), int(c[3:5], 16), int(c[5:7], 16))

empty_color = RGB(150, 150, 150)
classif_list = list(classif_dict.keys())

# classify leaves by the name of labels
for key in classif_list:
    for member_num in range(len(label_list)):
        member = label_list[member_num]
        if member.startswith(key):
            classif_dict[key][0].append(member_num)


## extract informations of orderings
# we can change orderings and labels by change this data

leaves_list = dn['leaves']
leaves_label = copy.deepcopy(label_list)

for leaf in range(len(leaves_list)):
    leaves_label[leaf] = label_list[leaves_list[leaf]]

## calculate coordinates of leaves and associate colors
node_list = [0 for i in leaves_list]

for cluster in classif_list:
    for member in classif_dict[cluster][0]: 
        
        # the index of our leaf
        member_index = int(leaves_list.index(member))
        
        # set the info of our leaf and learn it
        member_info = [member_index * 10 + 5, 0, classif_dict[cluster][1]]
        node_list[member] = member_info


## calculate coordinates of nodes and associate colors

for node_preinfo in Z:
    
    # the indices of left and right nodes
    left_node = int(node_preinfo[0])
    right_node = int(node_preinfo[1])
    
    # compute the x-coordinate of top-node
    node_xcoord = (node_list[left_node][0] + node_list[right_node][0]) / 2
    
    # set color of top-node
    if node_list[left_node][2] == node_list[right_node][2]:
        node_color = node_list[left_node][2]
    else:
        node_color = empty_color
    
    # memorize each info to node_list
    node_info = [node_xcoord, node_preinfo[2], node_color]
    node_list.append(node_info)



### draw dendrograms

## settings

# construct figure instance: prepare a whiteboard
fig = plt.figure(figsize = (18, 14))

# set font size
plt.rcParams["font.size"] = 12

# the width of lines
width_line = 3.0

# add an ax instance: prepare a space for a graph
ax = fig.add_subplot(1, 1, 1)

# set title and grid
#ax.set_title("Example for drawing dendrograms \n with many parameters", loc = "left", y = 1.02)
#ax.grid(axis = "y")

# set the range of horizontal axis
ax.set_xlim(-10, len(label_list) * 10 + 10)
ax.set_ylim(0, node_list[-1][1] * 1.1)

# set ticks on horizontal axis
ax.set_xticks(range(5, len(label_list) * 10 + 5, 10))

# change labels of ticks
ax.set_xticklabels(leaves_label, rotation = 90)
ax.tick_params(axis = "x", pad = 10)

# change distances between ticks and ax
#ax.tick_params(axis = "x", pad = 10)

# change distances between title and graph
ax.title.pad = 10


## draw parts

for konoji in range(len(Z)):
    node_preinfo = Z[konoji]
    left_node = int(node_preinfo[0])
    right_node = int(node_preinfo[1])
    top_node = konoji + len(leaves_list)
    
    # draw left vertical bar
    ax.plot([node_list[left_node][0], node_list[left_node][0]],
            [node_list[left_node][1], node_list[top_node][1]], 
            color = node_list[left_node][2],
            linewidth = width_line )
    
    # draw right vertical bar
    ax.plot([node_list[right_node][0], node_list[right_node][0]],
            [node_list[top_node][1], node_list[right_node][1]], 
            color = node_list[right_node][2],
            linewidth = width_line )
    
    # draw left and right parts of horizontal bar
    ax.plot([node_list[left_node][0], node_list[top_node][0]],
            [node_list[top_node][1], node_list[top_node][1]], 
            color = node_list[left_node][2],
            linewidth = width_line )
    ax.plot([node_list[top_node][0], node_list[right_node][0]],
            [node_list[top_node][1], node_list[top_node][1]], 
            color = node_list[right_node][2],
            linewidth = width_line )


## set colors of tick labels

# obtain label objects
labels_list = ax.xaxis.get_ticklabels()

# set colors
for cluster in classif_list:
    for member in classif_dict[cluster][0]:
        member_index = int(leaves_list.index(member))
        
        labels_list[member_index].set_color(node_list[member][2])
        
# label format
from matplotlib.ticker import FuncFormatter
def format_e(n, pos):
    return '$%.2f$' % (float(n)*0.0000001)

ax.yaxis.set_major_formatter(FuncFormatter(format_e))

plt.ylabel(r"distance ($\mathregular{ \times 10^7}$)",fontsize=30)
plt.xlabel('cell type',fontsize=30)

## Output
plt.savefig(output)

