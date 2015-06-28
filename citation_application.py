# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:30:27 2015

@author: jainstein
"""
import load_citation_data as load
import application_library as lib
from alg_dpa_trial import DPATrial

import numpy as np
import matplotlib.pyplot as plt

#%% Question 4 DPA Create DPA Graph
m = 13
n = 27770
DPA_graph = lib.make_random_graph_DPA(m,n)

#num_out_deg = 0
#for key in DPA_graph:
#    num_out_deg += len(DPA_graph[key])
#
#print num_out_deg


in_deg_dist_DPA = lib.in_degree_distribution(DPA_graph)
in_deg_DPA = lib.compute_in_degrees(DPA_graph)


#%% Part 1 Load Data
citation_graph = load.load_graph(load.CITATION_URL)
in_deg_dist = lib.in_degree_distribution(citation_graph)
in_deg = lib.compute_in_degrees(citation_graph)

#%%
num_out_deg = 0
for key in citation_graph:
    num_out_deg += len(citation_graph[key])

print num_out_deg


#%% Part 1 &  4

data = np.array(in_deg_dist.values())
norm_array = data/float(np.sum(data))
key_array = np.array(in_deg_dist.keys())

x = key_array
y = norm_array

data_DPA = np.array(in_deg_dist_DPA.values())
x_DPA = np.array(in_deg_dist_DPA.keys())
y_DPA = data_DPA/float(np.sum(data_DPA))

#%%
plt.loglog(x_DPA,y_DPA, 'bo')
plt.xlabel("In-Degree Number")
plt.ylabel("Normalized Number of Nodes")
plt.title("DPA In-Degree Distribution, log-log")

plt.savefig("part4.png", dpi=200)


#%% Part 5

citation, = plt.loglog(x,y,'s', mec = 'r', mfc='none', mew='1.5', label='Citation')
DPA, = plt.loglog(x_DPA,y_DPA,'.', mec = 'b', mfc='none', mew='1.5', label = "DPA")

plt.legend(handles = [citation, DPA])
plt.xlabel("In-Degree Number")
plt.ylabel("Normalized Number of Nodes")
plt.title("Citation vs. DPA In-Degree Distribution, log-log")

plt.savefig("part5.png", dpi=200)
#plt.savefig("part1.pdf")
#plt.savefig("part1.png", dpi=200)


#%%
from scipy import optimize

xdata = key_array
ydata = norm_array

logx = np.log10(xdata)
logy = np.log10(ydata)

fit_range = range(1,180)
plot_range = range(1,180)

fitfunc = lambda p, x: p[0] + p[1] * x 
errfunc = lambda p, x, y: (y - fitfunc(p, x))

out,success = optimize.leastsq(errfunc, [1,-1],args=(logx[fit_range], logy[fit_range]))

print "%g + %g*x"%(out[0],out[1])

logy_fit = out[1]*logx + out[0]

plt.plot(logx,logy,'ro')
plt.plot(logx[plot_range],logy_fit[plot_range],'b--', lw=3)
ax = plt.axes()
#ax.arrow(1.0, -3.5, 0.5, 0.4, head_width=0.05, head_length=0.1, fc='k', ec='k')
ax.annotate('Slope: %4.3f' %out[1], xy=(1.6, -2.7), xytext=(0.5, -3.5),
            arrowprops=dict(arrowstyle="simple"))

lx = plt.xlabel("log(In-Degree Number)")
ly = plt.ylabel("log(Normalized Number of Nodes)")
tl = plt.title("Citation In-Degree Distribution, log-log")
plt.ylim([-4.5,-0.5])

plt.savefig("part2_comp.png", dpi=200)


#plt.plot(x,y,'ro')
#plt.xlim([0,100])

#%%


logx_DPA = np.log10(x_DPA)
logy_DPA = np.log10(y_DPA)

fit_range = range(5,40)
plot_range = range(1,50)
fitfunc = lambda p, x: p[0] + p[1] * x 
errfunc = lambda p, x, y: (y - fitfunc(p, x))

out,success = optimize.leastsq(errfunc, [1,-1],args=(logx_DPA[fit_range], logy_DPA[fit_range]))

print "%g + %g*x"%(out[0],out[1])

logy_fit_DPA = out[1]*logx_DPA + out[0]


plt.plot(logx_DPA,logy_DPA,'bo')
plt.plot(logx_DPA[plot_range],logy_fit_DPA[plot_range],'m--', lw=3)
ax = plt.axes()
ax.annotate('Slope: %4.3f' %out[1], xy=(1.3, -2.7), xytext=(0.5, -3.5),
            arrowprops=dict(arrowstyle="simple"))
plt.ylim([-4.5,-0.5])

lx = plt.xlabel("log(In-Degree Number)")
ly = plt.ylabel("log(Normalized Number of Nodes)")
tl = plt.title("Citation In-Degree Distribution, log-log")

plt.savefig("part4_comp.png", dpi=200)



#%% Part 2
sample_graph = lib.make_complete_graph_prob(500,.5)
in_deg_dist_sample = lib.in_degree_distribution(sample_graph)

total_sample = float(sum(in_deg_dist_sample.values()))
norm_array_sample = np.array(in_deg_dist_sample.values())/total_sample
key_array_sample = np.array(in_deg_dist_sample.keys())
x_sample = key_array_sample
y_sample = norm_array_sample

plt.plot(x_sample,y_sample,'ro')
plt.title("N = 5000, p = %2.5f, $\lambda$ = %2.5f" %(num_plot[0],5000*num_plot[0]))





#%%

num_plot = [0.0001, 0.0005, 0.001, 0.01, 0.1, 0.5]

plt.figure(figsize=(12, 7))


for i in range(len(num_plot)):
    sample_graph = lib.make_complete_graph_prob(5000,num_plot[i])
    in_deg_dist_sample = lib.in_degree_distribution(sample_graph)
    
    data = np.array(in_deg_dist_sample.values())
    norm_array_sample = (data)/float(np.sum(data))
    key_array_sample = np.array(in_deg_dist_sample.keys())
    x_sample = key_array_sample
    #x_sample = (x_sample-np.mean(x_sample))/np.std(x_sample)
    y_sample = norm_array_sample
    plt.subplot(2,3,i+1)
    plt.loglog(x_sample,y_sample,'o')
    plt.xlabel("In Degree")
    plt.ylabel("Normalized Nuber of Nodes")
    plt.title("N = 5000, p = %2.4f, $\lambda$ = %4.4f" %(num_plot[i],4999*num_plot[i]))

plt.tight_layout()
#plt.savefig("part2.eps")
#plt.savefig("part2.pdf")
plt.savefig("part2_log.png", dpi=200)



