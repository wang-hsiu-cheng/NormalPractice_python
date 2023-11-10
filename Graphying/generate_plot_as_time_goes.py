import numpy as np
import matplotlib.pyplot as plt

# set graph style
plt.ion()
plt.figure(figsize=(8,2))
plt.xlim([0, 10])
plt.ylim([-1.5, 1.5])

# initialize variable
n = 100 # lenth variable
j = 0 # point distance variable
ideal_x = []
ideal_y = []
real_x = []
real_y = []
plt.ion()

for i in range(n):
    j += 0.1 #point distance

    # draw ideal line
    ideal_x.append(j)
    ideal_y.append(np.sin(j))

    # generate real point
    randomPoint_x = j + 0.1 * (np.random.rand(1) - 0.5 )
    randomPoint_y = np.sin(j) + 1 * (np.random.rand(1) - 0.5 )
    real_x.append(randomPoint_x)
    real_y.append(randomPoint_y)

    # plot point as time goes on
    plt.plot(ideal_x, ideal_y, color = "blue", lineWidth = 0.5)
    plt.scatter(real_x, real_y, s = 5, c = 'r', label="Fitting Curve", marker = 'o')
    plt.ioff()
    plt.pause(0.01)
plt.show()

