import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Watts-Strogatz
#Nodos
N = 100
#K vecinos cercanos
k = 4
#probabilidad
p = 0.60
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

# realambrar
for i in range(N):
    for j in range(1,k+1):
        if np.random.choice(prb):
            search = True
            while search:
                x = np.random.randint(N-1)
                y = np.random.randint(N-1)
                if x == y: #no puede conectarse consigo mismo
                    continue
                elif A[x,y] == 1: #no puede conectarse con una esquina ya ocupada
                    continue
                else:
                    A[i,(i-j)%N] = 0
                    A[x,y] = 1
                    search = False

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