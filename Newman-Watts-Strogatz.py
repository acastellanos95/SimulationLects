import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Newman-Watts-Strogatz
#Nodos
N = 20
#K vecinos cercanos
k = 2
#probabilidad
p = 0.30
prb = []
prb = [1]*int(p*100)
prb += [0]*int(abs(1-p)*100)
print(prb)

#Crear grafo mundo pequeño regular
A = np.zeros((N,N), dtype = int)

#Creando matriz de adyacencia del grafo mundo pequeño regular
for i in range(N):
    for j in range(1,k+1):
        A[i,(i+j)%N]=1
        A[i,(i-j)%N]=1
print(A)

#realambrar
for i in range(N):
    for j in range(N):
        if A[i,j] == 1:
            continue
        elif i == j:
            continue
        else:
            if np.random.choice(prb):
                A[i,j] = 1

#Funcion matriz a grafo
def from_matrix_to_graph(A):
    N = len(A)
    g = nx.Graph()
    for i in range(N):
        for j in range(i+1,N):
            if A[i,j] == 1:
                g.add_edge(i,j)
            else:
                continue
    return g

G = from_matrix_to_graph(A)
pos = nx.spring_layout(G)
nx.draw(G,pos)
plt.show()