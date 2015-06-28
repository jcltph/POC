# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 03:20:50 2015

@author: jainstein
"""

import random
from alg_upa_trial import UPATrial

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

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order
    
    
def fast_targeted_order(ugraph):
    
    new_graph = copy_graph(ugraph)
    
    n = len(new_graph.keys())
    degree_sets = [set() for i in range(n)]
    
    for index in range(n):
        node = new_graph.keys()[index]
        degree = len(new_graph[node])
        degree_sets[degree].add(node)
    
    order = []
    
    for dummy in range(n-1, -1, -1):

        while degree_sets[dummy]:
            random_node = random.choice(list(degree_sets[dummy]))
            degree_sets[dummy].remove(random_node)
            
            for neighbor in new_graph[random_node]:
                degree = len(new_graph[neighbor])
                new_graph[neighbor].remove(random_node)
                degree_sets[degree].remove(neighbor)
                degree_sets[degree-1].add(neighbor)
            
            order.append(random_node)
            del new_graph[random_node]

    return order
