import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

k=3.8
nIter=150
c=0.005

x = np.zeros((nIter,3,3))
x[0] = np.random.rand(3,3)
print(x[0])
for t in range(nIter-1):
    for i in range(3):
        for j in range(3):
            x[t+1,i,j] = (1-c)*k*x[t,i,j]*(1-x[t,i,j]) + (0.25)*c*(x[t,(i+1)%3,j%3] + x[t,i%3,(j+1)%3] 
            + x[t,(i-1)%3,j%3] + x[t,i%3,(j-1)%3])

fig = plt.figure()
sns.heatmap(x[0],cbar=True, cmap="Blues")
def animate(i):
    data = x[i]
    sns.heatmap(data, cbar=False, cmap = "Blues")
#Make animation
anim = animation.FuncAnimation(fig, animate,frames=nIter,interval=500, blit = False)
#Save Animation
anim.save("CoupledLattice.gif")
plt.show()
