"""
Created on Thu Jun 25 22:41:14 2015

@author: jainstein
"""
from collections import deque
import random
import alg_application2_provided as alg_provided

#%%
def bfs_visited(ugraph, start_node):
    """
    Takes the undirected graph ugraph and the node start_node and returns 
    the set consisting of all nodes that are visited by a breadth-first 
    search that starts at start_node
    """
    node_queue = deque([])
    visited = {start_node}
    node_queue.append(start_node)
    
    while node_queue:
        dummy_node = node_queue.popleft()
        for neighbor_node in ugraph[dummy_node]:
            if neighbor_node not in visited:
                visited.add(neighbor_node)
                node_queue.append(neighbor_node)
    
    return visited

#print bfs_visited(alg.GRAPH0, 0)

#%%
def cc_visited(ugraph):
    """
    Takes the undirected graph ugraph and returns a list of sets, where each 
    set consists of all the nodes (and nothing else) in a connected component, 
    and there is exactly one set in the list for each connected component in 
    ugraph and nothing else.
    """
    remaining_nodes = ugraph.keys()
    connected = []
    
    while remaining_nodes:
        current_node = random.choice(remaining_nodes)
        current_visited = bfs_visited(ugraph, current_node)
        connected.append(current_visited)
        remaining_nodes = list(set(remaining_nodes) - current_visited)
    
    return connected
    
#print cc_visited(alg.GRAPH3)

#%%
def largest_cc_size(ugraph):
    """
    Takes the undirected graph ugraph and returns the size (an integer) of 
    the largest connected component in ugraph.
    """
    visited = cc_visited(ugraph)
    cc_size = [len(cluster) for cluster in visited]
    if cc_size:
        max_cc_size = max(cc_size)
    else:
        max_cc_size = 0
    return max_cc_size
    
#print largest_cc_size(alg.GRAPH3)

#%%
def compute_resilience(ugraph, attack_order):
    """
    Takes the undirected graph ugraph, a list of nodes attack_order and 
    iterates through the nodes in attack_order.
    """
    max_connected_original = largest_cc_size(ugraph)
    #print "max_connected_original", max_connected_original
    max_connected = [max_connected_original]
    
    for attack_node in attack_order:        
        for dummy_nodes in ugraph[attack_node]:
            #print "dummy_nodes", dummy_nodes
            temp_value = ugraph[dummy_nodes]
            if attack_node in temp_value:
                temp_value.remove(attack_node)
                ugraph[dummy_nodes] = temp_value
        del ugraph[attack_node]
        temp_max_cc = largest_cc_size(ugraph)
        #print "temp_max_cc", temp_max_cc
        max_connected.append(temp_max_cc)
    
    return max_connected


#print compute_resilience(alg.GRAPH2, [1, 3, 5, 7, 2, 4, 6, 8])











