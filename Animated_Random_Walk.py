"""
DATE: NOV, 2018
PROGRAMA PARA HACER CAMINATAS ALEATORIAS SOBRE UN GRAFO DADO Y HACER UNA ANMIACION
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def random_walk(G,seed,steps):
    """ Funcion para realizar una caminata aleatorio en el grafo G.
        G     - grafo
        seed  - nodo inicial
        steps - numero de pasos

        La funcion regresa la lista de nodos que recorrio el caminante
    """

    track = [seed]

    for i in range(1,steps):
        track.append(np.random.choice(list(G.neighbors(track[i-1]))))

    return track

# Parametros
N     = 30      # Numero de nodos
steps = 60
seed  = np.random.choice(N-1)

G    = nx.erdos_renyi_graph(N,0.4)
pos  = nx.spring_layout(G)

path = random_walk(G,seed,steps)

print(path)

# Build plot
fig, ax = plt.subplots(figsize=(8,6))
plt.axis('off')

def update(num):

    ax.clear()

    # Background nodes
    null_nodes = nx.draw_networkx_nodes(G, pos=pos, nodelist=set(G.nodes()), node_color="white",  ax=ax)
    null_nodes.set_edgecolor("black")
    nx.draw_networkx_edges(G, pos=pos, ax=ax, edge_color="gray")

    nx.draw_networkx_labels(G, pos=pos, font_color="black", ax=ax)
    nx.draw_networkx_nodes(G, pos=pos, nodelist=[seed], node_color='red', ax=ax)
    
    for step_i in range(1,num):

        nx.draw_networkx_nodes(G, pos=pos, nodelist=[path[step_i-1]], node_color='lightcoral',ax=ax)
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[path[step_i]], node_color='red', ax=ax)
        nx.draw_networkx_edges(G, pos=pos, edgelist=[(path[step_i-1],path[step_i])], width=2., ax=ax)
        
        # Scale plot ax
        ax.set_title("Frame %d"%(step_i), fontweight="bold")
        ax.set_xticks([])
        ax.set_yticks([])

    nx.draw_networkx_nodes(G, pos=pos, nodelist=[path[0]], node_color='blue', ax=ax)
    plt.axis('off') 

ani = animation.FuncAnimation(fig, update, frames=len(path), interval=1000, repeat=True)
plt.show()

#triad = sequence_of_letters[i:i+3]
#path = ["O"] + ["".join(sorted(set(triad[:k + 1]))) for k in range(j)]

#     # Background nodes
#     nx.draw_networkx_edges(G, pos=pos, ax=ax, edge_color="gray")
#     null_nodes = nx.draw_networkx_nodes(G, pos=pos, nodelist=set(G.nodes()) - set(path), node_color="white",  ax=ax)
#     null_nodes.set_edgecolor("black")

#     # Query nodes
#     query_nodes = nx.draw_networkx_nodes(G, pos=pos, nodelist=path, node_color=idx_colors[:len(path)], ax=ax)
#     query_nodes.set_edgecolor("white")
#     nx.draw_networkx_labels(G, pos=pos, labels=dict(zip(path,path)),  font_color="white", ax=ax)
#     edgelist = [path[k:k+2] for k in range(len(path) - 1)]
#     nx.draw_networkx_edges(G, pos=pos, edgelist=edgelist, width=idx_weights[:len(path)], ax=ax)

#     # Scale plot ax
#     ax.set_title("Frame %d:    "%(num+1) +  " - ".join(path), fontweight="bold")
#     ax.set_xticks([])
#     ax.set_yticks([])