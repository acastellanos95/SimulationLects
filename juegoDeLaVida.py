import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import animation

N = 100
nIter = 50
CA = np.ndarray((nIter,N,N),dtype = int)

#Create array
for i in np.arange(nIter):
    CA[i] = np.zeros((N,N),dtype = int)


#Rule
def gameLife(c1,c2,c3,c4,c5,c6,c7,c8,c9):
    total = c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9
    if c1 == 1:
        if (total < 2) or (total > 3):
            return 0
        if (total == 2) or (total == 3):
            return 1
    elif c1 == 0:
        if (total == 3):
            return 1
        else:
            return 0


#randomize 1 and 0 in array
CA[0] = np.random.randint(low = 0, high = 2, size = (N,N), dtype = int)

#apply it
for j in range(nIter-1):
    for l in range(N):
        for m in range(N):

            CA[j+1,l,m] = gameLife(CA[j,l%N,m%N], CA[j,(l-1)%N,(m-1)%N], CA[j,(l-1)%N,(m)%N], CA[j,(l-1)%N,(m+1)%N],
                                    CA[j,(l)%N,(m-1)%N], CA[j,(l)%N,(m+1)%N], CA[j,(l+1)%N,(m-1)%N],CA[j,(l+1)%N,(m)%N],
                                    CA[j,(l+1)%N,(m+1)%N])

fig = plt.figure()

def animate(i):
    data = CA[i]
    sns.heatmap(data, cbar = False)
#Make animation
anim = animation.FuncAnimation(fig, animate,frames=np.arange(nIter), repeat = True)
#Save Animation
anim.save("Game_of_life.gif")
#Tarea https://www.binpress.com/simulating-segregation-with-python/