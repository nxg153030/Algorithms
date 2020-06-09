def depth_first_search(G):
    for v in G.vertices:
        v.color = 'white'
        v.predecessor = None

    for v in G.vertices:
        if v.color == 'white':
            dfs_visit(G, v)


def dfs_visit(G, vertex):
    vertex.color = 'gray'
    for u in G.adjacency_list[vertex]:
        if u.color == 'white':
            u.predecessor = vertex
            dfs_visit(G, u)
    vertex.color = 'black'
