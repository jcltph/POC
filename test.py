# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:55:20 2015

@author: jainstein
"""
        
"""  
with open('Q1_attempt1.pickle', 'w') as f:
    pickle.dump([citation_graph, citation_in_deg, in_deg_dist], f)

with open('Q1_attempt1.pickle') as f:
    citation_graph, citation_in_deg, in_deg_dist = pickle.load(f)
"""

import numpy as np

total = float(sum(in_deg_dist.values()))
norm_array = np.array(in_deg_dist.values())/total

key_array = np.array(in_deg_dist.keys())


import matplotlib.pyplot as plt
plt.plot(np.log10(key_array),np.log10(norm_array))


max(in_deg_dist.keys(),key=int)




total = float(sum(in_deg_dist.values()))
norm_array = np.array(in_deg_dist.values())/total
key_array = np.array(in_deg_dist.keys())

np.delete(norm_array, 0)
np.delete(key_array, 0)

x = np.log(np.delete(key_array, 0))
y = np.log(np.delete(norm_array, 0))

plt.plot(x,y,'ro')


plt.plot(key_array,norm_array,'r')


plt.plot(np.delete(key_array, 0),np.delete(norm_array, 0),'r')

max(in_deg_dist.keys(),key=int)