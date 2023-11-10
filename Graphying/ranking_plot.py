import matplotlib.pyplot as plt
from scipy.optimize import leastsq
import numpy as np

# make data
x = np.linspace(1, 5, 5) 
x1 = np.linspace(2, 5, 4) 
x21 = np.linspace(1, 2, 2)
x22 = np.linspace(5, 5, 1)
x3 = np.linspace(1, 11, 11)
x4 = np.linspace(13, 16, 4)
"""y = np.array([30, 44, 11, 54, 24, 31, 33, 34, 34, 42, 39]) #段考(前)
y1 = np.array([24, 54, 62, 36]) #段考(後)"""
y1 = np.array([9, 23, 8, 15, 43]) #數
y11 = np.array([93, 84, 90, 86, 80]) #數
y2 = np.array([17, 44, 9, 19]) #物
#y3 = np.array([34, 44, 83]) #化
y41 = np.array([5, 3]) #生
y42 = np.array([18]) #生
y5 = np.array([15, 24, 23, 61, 33]) #全

# plot
fig, ax = plt.subplots(ncols=1, figsize=(4, 4))
ax.plot(x, y1, 'o-', color="C0", label='math', linewidth=2.0) #數
#ax.plot(x1, y2, 'o-',color="C9", label='physics', linewidth=2.0) #物
#plt.plot(x2, y3,color="yellow", label='chemistry', linewidth=2.0) #化
#ax.plot(x21, y41, 'o-',color="C8", label='biology', linewidth=2.0) #生
#ax.plot(x22, y42, 'o-',color="C8", linewidth=2.0) #生
#ax.plot(x, y5,color="C3", label='whole', linewidth=5.0) #全
"""ax.plot(x3, y,color="blue", label = 'section exam', linewidth=2.0) #段考(前)
ax.plot(x4, y1,color="blue", linewidth=2.0) #段考(後)"""
ax.set(xlim=(0, 6), xticks=np.arange(0, 6),
       ylim=(100, 0))
"""ax.set(xlim=(0, 17), xticks=np.arange(0, 17),
       ylim=(100, 0))"""

plt.title(label="percentage ranking in the grade(math)", fontsize=15.0)
plt.xlabel('semester', fontsize=15.0)
plt.ylabel('percentage', fontsize=15.0)
plt.legend()
plt.show()
