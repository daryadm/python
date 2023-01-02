import random
from copy import deepcopy

def find_min_cut(edges, num_of_vertices):
    arcs = deepcopy(edges)
    while num_of_vertices > 2:
        rand_edge = random.choice(arcs)
        arcs.pop(edges.index(rand_edge)) # deleting first directed part of the contracted edge
        u = rand_edge[0]
        v = rand_edge[1]
        arcs.pop(arcs.index([v,u])) # deleting second directed part of the contracted edge
        num_of_vertices -= 1
        contracted_edges = []
        for e in arcs:
            edge = [v if x == u else x for x in e] # replacing contracted edge with the one that it is merging to
            if not [v,v] == edge: # we don't need self loops
                contracted_edges.append(edge)
        return find_min_cut(contracted_edges, num_of_vertices)
    return len(arcs)/2 # dividing by two because we count both directions

with open ('kargerMinCut.txt', 'r') as f:
    edges = []
    vertices_num = 0
    for line in f:
        vertices_num +=1
        vertices = [int(v) for v in line.split()]
        vertex_main = vertices[0]
        for vertex in vertices:
            if vertex == vertex_main:
                continue
            edges.append([vertex_main, vertex])

    min_cuts = []
    for i in range(0,200):
        min_cut = (find_min_cut(edges, vertices_num))
        min_cuts.append(min_cut)
    print(min(min_cuts))