import random

def find_min_cut(edges, num_of_vertices):
    while num_of_vertices > 2:
        rand_edge = random.choice(edges)
        edges.pop(edges.index(rand_edge))
        num_of_vertices -= 1
        u = rand_edge[0]
        v = rand_edge[1]
        contracted_edges = []
        for edge in edges:
            edge = [v if x == u else x for x in edge]
            if not [v,v] == edge:
                contracted_edges.append(edge)
        return find_min_cut(contracted_edges, num_of_vertices)
    return len(edges)

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
            edges.append((vertex_main, vertex))
    print(find_min_cut(edges, vertices_num))

    # 50 42 40
    # 