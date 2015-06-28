'''
Project 1 - Degree distributions for graphs
http://www.codeskulptor.org/#user40_ts5AARpzgl_1.py
'''

EX_GRAPH0 = {0: set([1,2]), 1: set([]),
             2: set([])}
EX_GRAPH1 = {0: set([1,4,5]), 1: set([2,6]),
             2: set([3]), 3: set([0]),
             4: set([1]), 5: set([2]),
             6: set([])}
EX_GRAPH2 = {0: set([1,4,5]), 1: set([2,6]),
             2: set([3,7]), 3: set([7]),
             4: set([1]), 5: set([2]),
             6: set([]), 7: set([3]),
             8: set([1,2]), 9: set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    '''
    construct complete graph for given number of nodes
    '''
    all_nodes = set(range(num_nodes))
    complete_graph = {}
    
    for node in range(num_nodes):
        temp_edge = all_nodes.difference(set([node]))
        complete_graph[node] = temp_edge

    return complete_graph


def compute_in_degrees(digraph):
    '''
    computes in degrees for a set of given nodes
    '''
    in_degrees = dict((deg, 0) for deg in digraph)
    
    for key in digraph:
        for node in digraph[key]:
            in_degrees[node] += 1

    return in_degrees


print compute_in_degrees(EX_GRAPH0)

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


print in_degree_distribution(EX_GRAPH0)