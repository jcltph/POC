'''
Project 1 - Degree distributions for graphs
http://www.codeskulptor.org/#user40_Zx0GZgcny6_22.py
'''
import random
from alg_dpa_trial import DPATrial

def make_complete_graph(num_nodes):
    '''
    construct complete directed graph for given number of nodes
    '''
    all_nodes = set(range(num_nodes))
    complete_graph = {}
    
    for node in range(num_nodes):
        temp_edge = all_nodes.difference(set([node]))
        complete_graph[node] = temp_edge

    return complete_graph

def make_complete_graph_prob(num_nodes, prob):
    '''
    construct complete directed graph for given number of nodes
    depending on probability p. Based on ER algorithm.
    '''
    all_nodes = set(range(num_nodes))
    complete_graph = {node: [] for node in all_nodes}
    
    for node in range(num_nodes):
        temp_edge = all_nodes.difference(set([node]))
        for pot_node in temp_edge:
            a = random.random()
            if a < prob:
                complete_graph[node].append(pot_node)
        
    return complete_graph


def make_random_graph_DPA(m,n):    
    random_graph = make_complete_graph(m)
    initial_graph = DPATrial(m)
    
    for i in range(n-m):
        new_node_neighbors = initial_graph.run_trial(m)
        random_graph[initial_graph._num_nodes-1] = new_node_neighbors
        
    return random_graph
    


def compute_in_degrees(digraph):
    '''
    computes in degrees for a set of given nodes
    '''
    in_degrees = {deg: 0 for deg in digraph}
    
    for key in digraph:
        for node in digraph[key]:
            in_degrees[node] += 1

    return in_degrees


def in_degree_distribution(digraph):
    '''
    computes the unnormalized distribution of 
    the in-degrees of the given directed graph
    '''
    in_deg_dist = {}
    in_degrees = compute_in_degrees(digraph)
    
    temp_collect = []
    
    for key in in_degrees:
        temp_collect += [in_degrees[key]]
    
    for deg in set(temp_collect):
        in_deg_dist[deg] = temp_collect.count(deg)

    return in_deg_dist
    

