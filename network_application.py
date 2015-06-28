"""
Created on Fri Jun 26 16:20:31 2015

@author: jainstein
"""
import random
import alg_application2_provided as alg_provided
import application2_library as library
from alg_upa_trial import UPATrial
import alg_module2_graphs as graph

import numpy as np
import matplotlib.pyplot as plt
#import time
import timeit
#import gc

#%% construct library functions necessary for the application first

def number_edges(ugraph):
    """
    calculate number of edges in undirected graph, ugraph in dictionary form
    """
    count = 0
    for key in ugraph:
        count += len(ugraph[key])
    return count
    
def edges_to_adj_list(num_nodes, edges):
    adj_list = {node: set() for node in range(num_nodes)}
    for edge in edges:
        adj_list[edge[0]].add(edge[1])
        adj_list[edge[1]].add(edge[0])
    return adj_list
    

def make_complete_graph(num_nodes):
    complete_graph = {node: set() for node in range(num_nodes)}
    for node in range(num_nodes):
        complete_graph[node] = set(range(num_nodes)) - set([node])
    
    return complete_graph


def construct_ER_graph(num_nodes, prob):
    all_pairs = []
    for node_1 in range(num_nodes):
        for node_2 in range(num_nodes):
            if node_2 != node_1:
                all_pairs.append(frozenset([node_1, node_2]))
    all_pairs = set(all_pairs)
    
    edges = []
    for pair in all_pairs:
        a = random.random()
        if a < prob:
            edges.append(list(pair)) 
            
    ER_graph = edges_to_adj_list(num_nodes, edges)    
    return ER_graph
    

def make_random_graph_UPA(m,n):    
    random_graph = make_complete_graph(m)
    for dummy in range(n-m):
        random_graph[dummy + m] = set()
        
    initial_graph = UPATrial(m)
    
    for dummy in range(n-m):
        new_node_neighbors = initial_graph.run_trial(m)
        random_graph[dummy + m] = new_node_neighbors
        for new_neighbor in new_node_neighbors:
            random_graph[new_neighbor].add(dummy + m)
        
    return random_graph



#%% Load network graph data 
network_graph = alg_provided.load_graph(alg_provided.NETWORK_URL)

# network graph has 1239 nodes and 3047 edges
    
print "network_graph", number_edges(network_graph)
print "network_graph", number_edges(network_graph)/2
# it prints out 6094 edges since each edge was counted twice for 
# undirected graph

#%% Construct ER and UPA sample graph for Part 1
n = 1239
m = 3
p = 0.00397

ER_graph = construct_ER_graph(n, p)
UPA_graph = make_random_graph_UPA(m,n)

print "ER_graph", number_edges(ER_graph)
print "ER_graph", number_edges(ER_graph)/2
print "UPA_graph", number_edges(UPA_graph)
print "UPA_graph", number_edges(UPA_graph)/2
 

#%% Part 1
def random_order(ugraph):
    nodes_random_order = ugraph.keys()
    random.shuffle(nodes_random_order)
    return nodes_random_order

network_copy = alg_provided.copy_graph(network_graph)
ER_copy = alg_provided.copy_graph(ER_graph)
UPA_copy = alg_provided.copy_graph(UPA_graph)

network_attack_order = random_order(network_copy)
ER_attack_order = random_order(ER_copy)
UPA_attack_order = random_order(UPA_copy)

resilience_network = library.compute_resilience(network_copy, network_attack_order)
resilience_ER = library.compute_resilience(ER_copy, ER_attack_order)
resilience_UPA = library.compute_resilience(UPA_copy, UPA_attack_order)

#%% Plot Results

data_attack_network = np.array(range(n+1))
data_attack_ER = np.array(range(n+1))
data_attack_UPA = np.array(range(n+1))

data_res_network = np.array(resilience_network)
data_res_ER = np.array(resilience_ER)
data_res_UPA = np.array(resilience_UPA)

linewidth = 2
network, = plt.plot(data_attack_network, data_res_network, 'r-', label = "Network", lw = linewidth)
er, = plt.plot(data_attack_ER, data_res_ER, 'b-', label = "ER, p = %1.5f" %p, lw = linewidth)
upa, = plt.plot(data_attack_UPA, data_res_UPA, 'g-', label = "UPA, m = %i" %m, lw = linewidth)

plt.legend(handles = [network, er, upa])
lx = plt.xlabel("Number of Nodes Removed")
ly = plt.ylabel("Size of the Largest Connected Component")
tl = plt.title("Graph Resilience, Random Attack")

#plt.savefig("part1.png", dpi=200)

#%% Question 2
num_nodes_removed = n * 0.2
num_nodes_remaining = n * 0.8

print "num_nodes_remaining", num_nodes_remaining
print "network", data_res_network[round(num_nodes_removed)]
print "ER", data_res_ER[round(num_nodes_removed)]
print "UPA", data_res_UPA[round(num_nodes_removed)]

#%% Question 3

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph



def fast_targeted_order(ugraph):
#    counter = 0
    new_graph = copy_graph(ugraph)
    
    n = len(new_graph.keys())
    degree_sets = [set() for i in range(n)]
    
    for index in range(n):
#        counter += 1
        node = new_graph.keys()[index]
        degree = len(new_graph[node])
        degree_sets[degree].add(node)
    
    order = []
    
    for dummy in range(n-1, -1, -1):

        while degree_sets[dummy]:
            random_node = random.choice(list(degree_sets[dummy]))
            degree_sets[dummy].remove(random_node)
            
            for neighbor in new_graph[random_node]:
#                counter += 1
                degree = len(new_graph[neighbor])
                new_graph[neighbor].remove(random_node)
                degree_sets[degree].remove(neighbor)
                degree_sets[degree-1].add(neighbor)
            
            order.append(random_node)
            del new_graph[random_node]
    
#    print counter
    return order


#ugraph = make_complete_graph(1000)
#print "number of edges", number_edges(ugraph)/2
#print "number of nodes", len(ugraph.keys())
#test = fast_targeted_order(ugraph)

targeted_order_network = fast_targeted_order(network_graph)
targeted_order_ER = fast_targeted_order(ER_graph)
targeted_order_UPA = fast_targeted_order(UPA_graph)

#%%

network_copy = alg_provided.copy_graph(network_graph)
ER_copy = alg_provided.copy_graph(ER_graph)
UPA_copy = alg_provided.copy_graph(UPA_graph)

resilience_targeted_network = library.compute_resilience(network_copy, targeted_order_network)
resilience_targeted_ER = library.compute_resilience(ER_copy, targeted_order_ER)
resilience_targeted_UPA = library.compute_resilience(UPA_copy, targeted_order_UPA)

#%% Plot Results

data_targeted_network = np.array(range(n+1))
data_targeted_ER = np.array(range(n+1))
data_targeted_UPA = np.array(range(n+1))

data_targeted_res_network = np.array(resilience_targeted_network)
data_targeted_res_ER = np.array(resilience_targeted_ER)
data_targeted_res_UPA = np.array(resilience_targeted_UPA)

linewidth = 2
network, = plt.plot(data_targeted_network, data_targeted_res_network, 'r-', label = "Network", lw = linewidth)
er, = plt.plot(data_targeted_ER, data_targeted_res_ER, 'b-', label = "ER, p = %1.5f" %p, lw = linewidth)
upa, = plt.plot(data_targeted_UPA, data_targeted_res_UPA, 'g-', label = "UPA, m = %i" %m, lw = linewidth)

plt.legend(handles = [network, er, upa])
lx = plt.xlabel("Number of Nodes Removed")
ly = plt.ylabel("Size of the Largest Connected Component")
tl = plt.title("Graph Resilience, Targeted Attack")

#%% Runtime Comparison
m_runtime = 5
num_average = 100

#gc.disable()
targeted_runtime = []
fast_targeted_runtime = []

for n in range(10, 1000, 10):
    UPA_graph_runtime = make_random_graph_UPA(m_runtime,n)
    
    time_sum = 0
    for dummy in range(num_average):
        start = timeit.default_timer()
        alg_provided.targeted_order(UPA_graph_runtime)
        stop = timeit.default_timer()
        time_sum += stop - start
    targeted_runtime.append(float(time_sum)/num_average)
    
    
for n in range(10, 1000, 10):
    UPA_graph_runtime = make_random_graph_UPA(m_runtime,n)
    
    time_sum = 0
    for dummy in range(num_average):
        start = timeit.default_timer()
        fast_targeted_order(UPA_graph_runtime)
        stop = timeit.default_timer()
        time_sum += stop - start
    fast_targeted_runtime.append(float(time_sum)/num_average)
    
#gc.enable()
    
    
#%%

linewidth = 2
targeted, = plt.plot(range(10, 1000, 10), targeted_runtime, 'r-', label = "Targeted", lw = linewidth)
fast_targeted, = plt.plot(range(10, 1000, 10), fast_targeted_runtime, 'b-', label = "Fast Targeted", lw = linewidth)

plt.legend(handles = [targeted, fast_targeted], loc = 2)
lx = plt.xlabel("Number of Nodes")
ly = plt.ylabel("Running Time (sec)")
tl = plt.title("Running Time with Input UPA Graph with m = %i" %m_runtime)
plt.savefig("part3_runtime.png", dpi=200)

#%%
plt.plot(range(10, 1000, 10), fast_targeted_runtime, 'b-', label = "Fast Targeted", lw = linewidth)

#%% Question 4

network_copy = alg_provided.copy_graph(network_graph)
ER_copy = alg_provided.copy_graph(ER_graph)
UPA_copy = alg_provided.copy_graph(UPA_graph)

targeted_order_network = alg_provided.targeted_order(network_graph)
targeted_order_ER = alg_provided.targeted_order(ER_graph)
targeted_order_UPA = alg_provided.targeted_order(UPA_graph)

resilience_targeted_network = library.compute_resilience(network_copy, targeted_order_network)
resilience_targeted_ER = library.compute_resilience(ER_copy, targeted_order_ER)
resilience_targeted_UPA = library.compute_resilience(UPA_copy, targeted_order_UPA)

#%% Plot Results

data_targeted_network = np.array(range(n+1))
data_targeted_ER = np.array(range(n+1))
data_targeted_UPA = np.array(range(n+1))

data_targeted_res_network = np.array(resilience_targeted_network)
data_targeted_res_ER = np.array(resilience_targeted_ER)
data_targeted_res_UPA = np.array(resilience_targeted_UPA)

linewidth = 2
network, = plt.plot(data_targeted_network, data_targeted_res_network, 'r-', label = "Network", lw = linewidth)
er, = plt.plot(data_targeted_ER, data_targeted_res_ER, 'b-', label = "ER, p = %1.5f" %p, lw = linewidth)
upa, = plt.plot(data_targeted_UPA, data_targeted_res_UPA, 'g-', label = "UPA, m = %i" %m, lw = linewidth)

plt.legend(handles = [network, er, upa])
lx = plt.xlabel("Number of Nodes Removed")
ly = plt.ylabel("Size of the Largest Connected Component")
tl = plt.title("Graph Resilience, Targeted Attack")

#plt.savefig("part4.png", dpi=200)

#%% Question 5
num_nodes_removed = n * 0.2
num_nodes_remaining = n * 0.8

print "num_nodes_remaining", num_nodes_remaining
print "network", data_targeted_res_network[round(num_nodes_removed)]
print "ER", data_targeted_res_ER[round(num_nodes_removed)]
print "UPA", data_targeted_res_UPA[round(num_nodes_removed)]
