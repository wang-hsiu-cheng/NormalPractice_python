import numpy as np
import matplotlib.pyplot as plt

# set graph style
plt.ion()
plt.figure(figsize=(8,2))
plt.xlim([0, 10])
plt.ylim([-1.5, 1.5])

# draw ideal line
ideal_x = np.linspace(0, 10, 100)
ideal_y = np.sin(ideal_x)
plt.plot(ideal_x, ideal_y, color = "blue", lineWidth = 0.5)

# initialize variable
n = 100 # lenth variable
j = 0 # point distance variable
em_filter = True
alpha_EMF = 0.1 # EMF parameter
oe_filter = True
t_e = 0.1
x_dot = 0
f_c_min = 1 # OEF parameter
beta = 0.5 # OEF parameter
f_c = 0
alpha_OEF = 0
real_x = []
real_y = []
em_filter_x = []
em_filter_y = []
oe_filter_x = []
oe_filter_y = []
plt.ion()

for i in range(n):
    j += 0.1 #point distance

    # generate real point
    randomPoint_x = j + 0.1 * (np.random.rand(1) - 0.5 )
    randomPoint_y = np.sin(j) + 1 * (np.random.rand(1) - 0.5 )
    real_x.append(randomPoint_x)
    real_y.append(randomPoint_y)

    # generate filtered point
    if em_filter :
        em_filter_x.append(real_x[i])
        if i > 0 :
            filterPoint_y = alpha_EMF * real_y[i] + (1 - alpha_EMF) * em_filter_y[i - 1]
        else :
            filterPoint_y = real_y[i]
        em_filter_y.append(filterPoint_y)
    if oe_filter :
        oe_filter_x.append(real_x[i])
        if i > 0 :
            f_c = f_c_min + beta * real_y[i]
            alpha_OEF = 1 / (1 + 1 / (2 * np.pi * 0.1 * f_c))
            filterPoint_y = alpha_OEF * real_y[i] + (1 - alpha_OEF) * oe_filter_y[i - 1]
        else :
            filterPoint_y = real_y[i]
        oe_filter_y.append(filterPoint_y) 

    # plot point as time goes on
    plt.scatter(real_x, real_y, s = 5, c = 'r', label="Fitting Curve", marker = 'o')
    if em_filter :
        plt.plot(em_filter_x, em_filter_y, color = "C2", lineWidth = 1)
    if oe_filter :
        plt.plot(oe_filter_x, oe_filter_y, color = "C9", lineWidth = 1)
    plt.ioff()
    plt.pause(0.01)
plt.show()

