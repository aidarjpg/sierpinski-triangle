from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math
from random import randint

fig, ax = plt.subplots()
x, y = [0.0, 3.0, 6.0, 4.0],[0.0, 3*math.sqrt(3), 0.0, 3.0]
sc = ax.scatter(x,y, s=1)
i = 3
def plotmid(i, coef):
    while(i<=10000):
        value = randint(0, 2) #choose random point 
        x.append((x[value] + x[i])*coef) #find midX
        y.append((y[value] + y[i])*coef) #find midY
        sc.set_offsets(np.c_[x,y]) #plot midPoint
        i = i + 1

def main():
    ani = FuncAnimation(plt.gcf(), plotmid(i, 0.5), interval = 10, repeat=True)
    plt.show()
    
if __name__ == "__main__":
    main()