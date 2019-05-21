def main():
    import numpy as np
    import random
    import seaborn as sns
    import matplotlib.pyplot as plt
    from matplotlib import animation

    #Create Agents
    Empty = 0

    #Create city with NxN places to live
    N = 20
    nIter = 50
    city = np.ndarray((nIter,N,N),dtype = int)

    #begin with empty houses
    for i in np.arange(nIter):
        city[i] = np.zeros((N,N),dtype = int)
    
    pop = [0]*30 + [1]*35 + [2]*35

    for n_i in range(N):
        for n_j in range(N):
            city[0,n_i,n_j] = np.random.choice(pop)

    #rules
    def lHappiness(center,upLeft,up,upRight,left,right,botLeft,bot,botRight):
        #treshold of segregation
        tresh = 0.4
        #counts of similarity
        nSim = 0
        nDif = 0
        for j in [upLeft,up,upRight,left,right,botLeft,bot,botRight]:
            if (j == center):
                nSim += 1
                #print(nSim)
            else:
                nDif +=1
                #print(nDif)
        if (nSim + nDif) == 0:
            return False
        else:
            return (nSim/(nSim + nDif)) > tresh
    
    for k in range(nIter-1):
        for l in range(N):
            for m in range(N):
                #if this part is empty we want to continue with the next point
                if city[k,l,m] == Empty:
                    continue
                #if its happy then continue with the next point
                elif lHappiness(city[k,l,m],city[k,(l-1)%N,(m-1)%N],city[k,(l-1)%N,(m)%N],city[k,(l-1)%N,(m+1)%N],city[k,(l)%N,(m-1)%N],city[k,(l)%N,(m+1)%N],city[k,(l+1)%N,(m-1)%N],city[k,(l+1)%N,(m)%N],city[k,(l+1)%N,(m+1)%N]) == True:
                    continue
                #if its not happy then move
                elif lHappiness(city[k,l,m],city[k,(l-1)%N,(m-1)%N],city[k,(l-1)%N,(m)%N],city[k,(l-1)%N,(m+1)%N],city[k,(l)%N,(m-1)%N],city[k,(l)%N,(m+1)%N],city[k,(l+1)%N,(m-1)%N],city[k,(l+1)%N,(m)%N],city[k,(l+1)%N,(m+1)%N]) == False:
                    newPosBool = True
                    while(newPosBool):
                        newX = random.randint(0,N-1)
                        newY = random.randint(0,N-1)
                        if (city[k,newX,newY] == Empty):
                            city[k,newX,newY] = city[k,l,m]
                            city[k,l,m] = 0
                            newPosBool = False
        city[k+1] = city[k]
    
    fig = plt.figure()

    def animate(i):
        data = city[i]
        sns.heatmap(data, cbar = False,cmap = "Blues")
    #Make animation
    anim = animation.FuncAnimation(fig, animate,frames=np.arange(nIter), repeat = True)
    #Save Animation
    anim.save("Schelling.gif")
    


if __name__ == "__main__":
    main()
