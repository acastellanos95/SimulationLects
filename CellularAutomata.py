import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")

## Número de celdas e iteraciones
num_celda = 100
num_it = 50

##Crear la matriz de ceros
CA = np.zeros((num_it,num_celda))
CA[0][(num_celda-1)//2]=1

##Definir regla
def Rule_30(c1,c2,c3):
    if c1 == 1 and c2 == 1 and c3 == 1:
        return 0
    if c1 == 1 and c2 == 1 and c3 == 0:
        return 0
    if c1 == 1 and c2 == 0 and c3 == 1:
        return 0
    if c1 == 1 and c2 == 0 and c3 == 0:
        return 1
    if c1 == 0 and c2 == 1 and c3 == 1:
        return 1
    if c1 == 0 and c2 == 1 and c3 == 0:
        return 1
    if c1 == 0 and c2 == 0 and c3 == 1:
        return 1
    if c1 == 0 and c2 == 0 and c3 == 0:
        return 0

##Aplicar la regla
for t in np.arange(num_it-1):
    for j in np.arange(num_celda):
        CA[t+1][j] = Rule_30(CA[t][(j-1)%num_celda],CA[t][j%num_celda],CA[t][(j+1)%num_celda])

##Graficar
sns.heatmap(CA)
plt.show()
