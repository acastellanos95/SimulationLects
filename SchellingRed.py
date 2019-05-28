import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from barabassi import barabassi_graph_andre
from matplotlib import animation

#Number of people
N = 35
#Number of agents (recommended = 2 )
a = 2
#Proportions == 100%(list) of empty, agent 1, agent 2
p = [30,35,35]
#Creating list with proportions
pop = []
for n in range(a+1):
    pop += [n]*p[n]
#Number of iterations
num = 70

def from_matrix_to_graph(A):
        N = len(A)
        g = nx.Graph()
        for i in range(N):
            for j in range(i+1,N):
                if A[i,j] == 1:
                    g.add_edge(i,j)
        return g

#create random graph
def random_graph_andre(N):
    A = np.zeros((N,N))
    for i in range(N):
        for j in range(i+1,N):
            A[i,j] = np.random.randint(2)
    G = from_matrix_to_graph(A)
    return G

#introduce population
def populate(G,l):
    """
    G: Graph
    l: list with 100 element that was created with pop
    """
    print(list(G.nodes))
    for i in list(G.nodes):
        G.nodes[i]["type"] = np.random.choice(l)
    return G

def happiness(G,node,tresh):
    nSim = 0
    nDif = 0
    for j in G.neighbors(node):
        if (G.nodes[j]["type"] == G.nodes[node]["type"]):
            nSim += 1
            #print(nSim)
        else:
            nDif +=1
            #print(nDif)
    return (nSim/(nSim + nDif)) > tresh

listGraph = [] 
def Schelling_red_andre(G):
    tresh = 0.4
    G = populate(G,pop)
    listGraph = [G]
    print(list(G.nodes))
    for n in range(num):
        for i in range(1,N-1):
            if happiness(G, i, tresh) == True:
                continue
            elif happiness(G, i, tresh) == False:
                newPosBool = True
                while(newPosBool):
                    l = np.random.randint(1,N-1)
                    if G.nodes[l]["type"] == 0:
                        G.nodes[l]["type"] = G.nodes[i]["type"]
                        G.nodes[i]["type"] = 0
                        newPosBool = False
                    else:
                        continue
        listGraph.append(G)
        pos = nx.spring_layout(G)
        nx.draw(G, pos)
        node_labels = nx.get_node_attributes(G,'type')
        nx.draw_networkx_labels(G, pos,labels = node_labels)
        plt.show()


G1 = barabassi_graph_andre(N, 4)
Schelling_red_andre(G1)
#print(G.edges)
"""pos = nx.spring_layout(G)
nx.draw(G, pos)
node_labels = nx.get_node_attributes(G,'type')
nx.draw_networkx_labels(G, pos,labels = node_labels)
plt.show()
pos = nx.spring_layout(G1)
nx.draw(G1, pos)
node_labels = nx.get_node_attributes(G1,'type')
nx.draw_networkx_labels(G1, pos,labels = node_labels)
plt.show()"""
"""fig = plt.figure()

def animate(i):
    data = G
    pos = nx.spring_layout(data)
    node_labels = nx.get_node_attributes(data,'type')
    nx.draw_networkx_labels(data, pos,labels = node_labels)
#Make animation
anim = animation.FuncAnimation(fig, animate,frames=num-1, repeat = True)
plt.show()
#Save Animation
#anim.save("SchellingRed.gif")"""
    
