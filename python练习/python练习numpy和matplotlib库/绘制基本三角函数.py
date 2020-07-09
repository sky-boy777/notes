import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,6,100)
y=np.cos(2*np.pi*x)*np.exp(-x)+0.8
plt.plot(x,y,'k',color='b',linewidth=1,linestyle='-.')
plt.show()
