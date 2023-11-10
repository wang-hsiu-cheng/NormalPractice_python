import matplotlib.pyplot as plt
import numpy as np

# make data:
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
x = 1 + np.arange(6)
y = np.array([85, 78, 87, 93, 78, 80])

# plot
fig, ax = plt.subplots()
ax.grid(True, linestyle='-.')
rects1 = ax.bar(x, y, width=0.5, edgecolor="white", linewidth=1)
ax.set(xlim=(0, 7), xticks=np.arange(0,7),
       ylim=(0, 100))
ax.set_ylabel('Scores')
ax.set_title('the scores of each special class')
ax.set_xticks(x)
ax.bar_label(rects1, padding=3)
fig.tight_layout()
plt.show()
