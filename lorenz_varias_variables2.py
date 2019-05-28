import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import h5py

N = 20
# Time arange
time = np.arange(0.0,100.0, 0.01)

# Initial condition
#state0 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]
state0 = np.random.normal(loc = 15.0,scale = 5.0,size=3*N)
print(state0)

#global c
c = 0.8

#gammas

g1, g2, g3=1,1,1

# -----------------------------------------------------------------------------------------------------------------
#                                             FUNCTIONS
# -----------------------------------------------------------------------------------------------------------------

def rk4(f,x0,t):
    
    """Fourth-order Runge-Kutta method to solve x' = f(x,t) with x(t[0]) = x0 """

    n = len( t )
    x = np.array( [ x0 ] * n )
    for i in range( n - 1 ):
        h = t[i+1] - t[i]
        k1 = h * f(x[i],t[i])
        k2 = h * f( x[i] + 0.5 * k1, t[i] + 0.5 * h)
        k3 = h * f( x[i] + 0.5 * k2, t[i] + 0.5 * h)
        k4 = h * f( x[i] + k3, t[i+1])
        x[i+1] = x[i] + ( k1 + 2.0 * ( k2 + k3 ) + k4 ) / 6.0

    return x

G = nx.barabasi_albert_graph(N, 2)
A = nx.to_numpy_matrix(G)
for i in range(N): 
    A[i,i] = -G.degree(i)

print('-----\n',A)

def NetLorenz(state,t):
    odes = []
    for j in range(N):
        x_i = state[3*j]
        y_i = state[3*j+1]
        z_i = state[3*j+2]

        sumax = sum([c*A[j,l]*state[3*l] for l in range(N)])
        sumay = sum([c*A[j,l]*state[3*l+1] for l in range(N)])
        sumaz = sum([c*A[j,l]*state[3*l+2] for l in range(N)])
          
        odes.append(10*(y_i-x_i)     + sumax*g1)
        odes.append(x_i*(28-z_i)-y_i + sumay*g2)
        odes.append(y_i*x_i-2.6*z_i  + sumaz*g3)

    return np.array(odes)

state = rk4(NetLorenz,state0,time)
print(state)
"""h5f = h5py.File('Lorenzdata.h5', 'w')
h5f.create_dataset('dataset_1', data=state)
h5f.create_dataset('dataset_2', data=G)
h5f.close()"""
fig, axes = plt.subplots(1,4, figsize=(12, 4))
axes[0].plot(time,state[:,0]-state[:,3],label="x_1")
axes[0].plot(time,state[:,3]-state[:,6],label="x_2")
axes[0].plot(time,state[:,6]-state[:,0],label="x_3")
axes[0].set_title("x_1, x_2, x_3 contra t")
axes[0].legend()

axes[1].plot(time,state[:,1]-state[:,4],label="y_1")
axes[1].plot(time,state[:,4]-state[:,7],label="y_2")
axes[1].plot(time,state[:,7]-state[:,1],label="y_3")
axes[1].set_title("y_1, y_2, y_3 contra t")
axes[1].legend()

axes[2].plot(time,state[:,2]-state[:,5],label="z_1")
axes[2].plot(time,state[:,5]-state[:,8],label="z_2")
axes[2].plot(time,state[:,8]-state[:,2],label="z_3")
axes[2].set_title("z_1, z_2, z_3 contra t")
axes[2].legend()

axes[3].plot(state[:,0],state[:,1],label="Lorenz1")
axes[3].plot(state[:,3],state[:,4],label="Lorenz2")
axes[3].plot(state[:,6],state[:,7],label="Lorenz3")
axes[3].set_title("Espacio fase de Lorenz1, Lorenz2, Lorenz3")
axes[3].legend()

plt.show()