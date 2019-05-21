import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

def barabassi_graph_andre(n,m):
    G = nx.Graph()
    G.add_edges_from([(1,2), (2,3), (1,3)])
    counter = 0
    prob_list = []
    for i in range(4,n):
        G.add_node(i)
    for node in range(4,n):
        for node_iter in range(1,node):
            for node_multiply in range(G.degree(node_iter)):
                prob_list.append(node_iter)
        while not counter == m:
            G.add_edge(node,int(random.choice(prob_list)))
            counter +=1
        counter = 0
        prob_list = []
    print(list(G.neighbors(1)))
    nx.draw(G)
    plt.show()
        
if __name__ == "__main__":
    barabassi_graph_andre(40,2)