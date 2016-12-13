import networkx
import urllib2
homer = urllib2.urlopen('http://people.sc.fsu.edu/~jburkardt/datasets/sgb/homer.dat')

def read_nodes(gfile):
    """Reads in the nodes of the graph from the input file.
    
    Args:
        gfile: A handle for the file containing the graph data, starting at the top.
        
    Returns:
        A generator of the nodes in the graph, yielding a list of the form:
            ['CH', 'AG, 'ME', ...]
    """
    # TODO: implement function
    nodes = [] 
    
    # read in the lines then parse each one for the node
    gf_local = urllib2.urlopen(gfile.url)
    f = gf_local.readlines()
    for line in f:
        tokens = line.split()
        if len(tokens) > 0:
            if tokens[0] != '*':            
                if len(tokens[0]) == 2:
                    nodes.append(tokens[0])
        
    return nodes 

def read_edges(gfile):
    """Reads in the edges of the graph from the input file.
    
    Args:
        gfile: A handle for the file containing the graph data, starting at the top 
            of the edges section.
            
    Returns:
        A generator of the edges in the graph, yielding a list of pairs of the form:
            [('CH', 'AG'), ('AG', 'ME'), ...]
    """
    # TODO: implement function
    edgesets = []
    edges = [] 
    
    # read in the lines then parse each one for the node
    gf_local = urllib2.urlopen(gfile.url)
    f = gf_local.readlines()
    for line in f:
        tokens = line.split()
        if len(tokens) > 0:
            if tokens[0] != '*':            
                if len(tokens[0]) != 2:                   
                    for edgeset in tokens[0].split(':')[1].split(';'):                                        
                        edgesets.append(edgeset.split(','))
                        
    for edgeset in edgesets:
        for i in range(0, len(edgeset)):
            for j in range(i + 1, len(edgeset)):
                e = (edgeset[i], edgeset[j])
                edges.append(e)                
    return edges

import networkx as nx
G = nx.Graph()
G.add_nodes_from(read_nodes(homer))
G.add_edges_from(read_edges(homer))

def Search(graph, root):
    """Runs depth-first search through a graph, starting at a given root. Neighboring
    nodes are processed in alphabetical order.
    
    Args:
        graph: the given graph, with nodes encoded as strings.
        root: the node from which to start the search.
        
    Returns:
        A list of nodes in the order in which they were first visited.
    """
    # TODO: implement function
    for node in graph.nodes():    
        graph.node[node]['color'] = "W"
        graph.node[node]['predecessor'] = None
    time = 0
    return DFS(graph, root, time)
    
def DFS(graph, node, time):
    
    visited = []
    time += 1
    graph.node[node]['discovered'] = time
    graph.node[node]['color'] = "G"
    visited.append(node)
    
    for neighbor in sorted(graph.neighbors(node)):
        if graph.node[neighbor]['color'] == "W":
            graph.node[neighbor]['predecessor'] = graph.node[node] 
            visited.extend(DFS(graph, neighbor, time))
    
    graph.node[node]['color'] = "B"
    time += 1
    graph.node[node]['finished'] = time
    return visited

ulysses = Search(G, 'OD')

def connected_components(graph):
    """Computes the connected components of the given graph.
    
    Args: 
        graph: the given graph, with nodes encoded as strings.
        
    Returns:
        The connected components of the graph. Components are listed in
        alphabetical order of their root nodes.
    """
        
    # TODO: implement function
    component_roots = []
    node_list = sorted(graph.nodes())
    while(len(graph.nodes()) > 0):
        node_list = sorted(graph.nodes()) 
        component = Search(graph, node_list[0])
        component_roots.append(component)
        graph.remove_nodes_from(component)
        
    return sorted(component_roots)

character_interactions = connected_components(G)

component_sizes = [len(c) for c in character_interactions]
print "There are 12 connected components in the Iliad:", len(component_sizes) == 12
print "The giant component has size 542:", max(component_sizes) == 542
print "There are 5 isolated characters:", len([c for c in component_sizes if c == 1]) == 5



