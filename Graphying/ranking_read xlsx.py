import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5,6])
y=np.array([9,23,8,15,43,0])

plt.figure(figsize=(8,6))
plt.scatter(x,y,color="red",label="Sample Point",linewidth=3)
plt.show()
