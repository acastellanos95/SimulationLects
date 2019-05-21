def main(N,k):
    import numpy as np
    import networkx as nx
    import matplotlib.pyplot as plt
    """
    N: int, dimension squared array
    """
    #crear matriz 
    # 0 1 1 0 0 0 0 0 1 1
    # 1 0 1 1 0 0 0 0 0 1
    # 1 1 0 1 1 0 0 0 0 0
    # ...
    A = np.zeros((N,N), dtype = int)

    for i in range(N):
        for j in range(1,k+1):
            A[i,(i+j)%N]=1
            A[i,(i-j)%N]=1
    print(A)
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

    g1 = from_matrix_to_graph(A)
    #pos = nx.circular_layout(g1)
    nx.draw(g1, with_labels = True)
    plt.show()

    def degree_hist(G):
        list1 = G.degree()
        list2 = []
        list3 = []
        for i in list1:
            list2.append(i[0])
            list3.append(i[1])
        plt.scatter(list2,list3)
        plt.show()
    
    print(nx.degree(g1))
    return g1, degree_hist(g1) 


if __name__ == "__main__":
    test = main(16,3)