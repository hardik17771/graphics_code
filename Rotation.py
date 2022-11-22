import matplotlib.pyplot as plt
import math

import numpy as np
pi=3.1416
x1=int(input("x1: "))
y1=int(input("y1: "))
x2=int(input("x2: "))
y2=int(input("y2: "))
x3=int(input("x3: "))
y3=int(input("y3: "))
X = [x1, x2, x3, x1]
Y = [y1, y2, y3, y1]

theta = float(input("Enter rotating variable "))


s = math.sin(math.radians(theta))
c = math.cos(math.radians(theta))

X_new = []
Y_new = []

R = [0, 0, 0]
T = [[c, -s, 0],
     [s, c, 0],
     [0, 0, 1]]


for i in range(len(X)):
    B = [X[i], Y[i], 1]
    R = np.dot(T, B)
    X_new.append(R[0])
    Y_new.append(R[1])

fig = plt.figure()
plt.plot(X, Y, X_new, Y_new)
plt.show()