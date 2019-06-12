import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from barabassi import barabassi_graph_andre
from matplotlib import animation

#Grafo
G = barabassi_graph_andre(50,3)
#Número inicial de personas infectadas
N_inf = 3
#Probabilidad de infección
Prob = 0.15
#lista probabilidar
prb = []
prb = [1]*int(Prob*100)
prb += [0]*int(abs(1-Prob)*100)
print(prb)
#Dias infectados
D = 6
#Dias iteración
Days_iter = 15
#lista de infectados
inf = []
#lista de inmunes
imm = []
#lista de no infectados
uninf = []

#Desinfectar
print(list(G.nodes))
for i in list(G.nodes):
    G.nodes[i]["Days"] = 0
    G.nodes[i]["Infected"] = 0
    G.nodes[i]["Immune"] = 0

#Infectar
for i in np.random.randint(max(G.nodes),size=N_inf):
    G.nodes[i]["Infected"] = 1
print(G.nodes(data=True))
#definimos posicion inicial
pos = nx.spring_layout(G)

fig, ax = plt.subplots(figsize=(8,6))
plt.axis('off')

#Iterar
def animate(i):
    for j in G.nodes:
        if G.nodes[j]["Infected"] == 0 and G.nodes[j]["Immune"] == 0:
            uninf.append(j)
        elif G.nodes[j]["Infected"] == 1 and G.nodes[j]["Immune"] == 0 and G.nodes[j]["Days"] <= D:
            for k in G.neighbors(j):
                if G.nodes[k]["Immune"] == 0 and G.nodes[k]["Infected"] == 0:
                    G.nodes[k]["Infected"] = np.random.choice(prb)
            if G.nodes[j]["Days"] >= 6:
                G.nodes[j]["Infected"] = 0
                G.nodes[j]["Immune"] = 1
                imm.append(j)
                inf.remove(j)
            G.nodes[j]["Days"] +=1
            print(G.nodes[j]["Days"])
            inf.append(j)
    nx.draw(G, pos)
    node_labels = nx.get_node_attributes(G,'Infected')
    nx.draw_networkx_nodes(G, pos=pos, nodelist=uninf, node_color='lightcoral', ax=ax)
    nx.draw_networkx_nodes(G, pos=pos, nodelist=inf, node_color='red',ax=ax)
    nx.draw_networkx_nodes(G, pos=pos, nodelist=imm, node_color='blue', ax=ax)

    ax.set_title("Día %d"%(i), fontweight="bold")
    

ani = animation.FuncAnimation(fig, animate, frames=Days_iter, interval=1000)
plt.show()
