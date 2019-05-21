import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def Graph_erdos_renyi(prob, N):
    """
    prob: (0.0,1.0)
    N: dimension
    """
    
    A = np.zeros((N,N))
    for i in range(N):
        for j in range(i+1,N):
            random = np.random.uniform(0.0,1.0)
            if random < prob:
                A[i,j] = 1
                A[j,i] = 1
            else:
                continue
    return A

def from_matrix_to_graph(A):
        N = len(A)
        g = nx.Graph()
        for i in range(N):
            for j in range(i+1,N):
                if A[i,j] == 1:
                    g.add_edge(i,j)
        return g

def degree_hist(G):
    a = [sorted(v for (u,v) in G.degree())]
    plt.hist(a)
    plt.show()

M = Graph_erdos_renyi(0.5,30)
g = from_matrix_to_graph(M)
#degree_hist(g)
nx.draw_spring(g)
plt.show()
print(g.subgraph(c) for c in nx.connected_components(g))