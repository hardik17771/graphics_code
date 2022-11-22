import matplotlib.pyplot as plt

x_cent = int(input("Enter x-coordinates of the center: "))
y_cent = int(input("Enter y-coordinates of the center: "))
r = int(input("Enter the radius of the circle: "))

x_quad1 = []
y_quad1 = []
decor = []

x_init = 0
y_init = r
decision_parameter = 3 - 2*r


x = x_init
y = y_init
p = decision_parameter

while(x < y):
  
    if p < 0:
        x += 1
        p += 6 + 4 * x
    else:
        x += 1
        y -= 1
        p += 10 - 4 * y + 4 * x
    x_quad1.append(x)
    y_quad1.append(y)
    

x_oct2=[]
y_oct2=[]

for i in range(len(x_quad1)):
    x_oct2.append(y_quad1[i])
    y_oct2.append(x_quad1[i])
    
x_oct2.reverse()
y_oct2.reverse()

for i in range(len(x_quad1)):
    x_quad1.append(x_oct2[i])
    y_quad1.append(y_oct2[i])
    
x_quad2 = [(x_cent - x) for x in x_quad1]
y_quad2 = [(y_cent + y) for y in y_quad1]

x_quad3 = [(x_cent - x) for x in x_quad1]
y_quad3 = [(y_cent - y) for y in y_quad1]

x_quad4 = [(x_cent + x) for x in x_quad1]
y_quad4 = [(y_cent - y) for y in y_quad1]

x_quad1 = [(x_cent + x) for x in x_quad1]
y_quad1 = [(y_cent + y) for y in y_quad1]

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(x_quad1, y_quad1, x_quad2, y_quad2, x_quad3, y_quad3, x_quad4, y_quad4)
ax.set_aspect('equal', adjustable='box')
plt.title("Bresenham Circle Drawing Algorithm")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()




x_trans=int(input("x-coordinate "))
y_trans=int(input("y-coordinate "))


x_cent += x_trans
y_cent += y_trans

x_quad1_new = []
y_quad1_new = []
decor = []

x_init = 0
y_init = r
decision_parameter = 3 - 2*r

x = x_init
y = y_init
p = decision_parameter

while(x < y):
  
    if p < 0:
        x += 1
        p += 6 + 4 * x
    else:
        x += 1
        y -= 1
        p += 10 - 4 * y + 4 * x
    x_quad1_new.append(x)
    y_quad1_new.appen(y)
    

x_oct2=[]
y_oct2=[]

for i in range(len(x_quad1_new)):
    x_oct2.append(y_quad1_new[i])
    y_oct2.append(x_quad1_new[i])
    
x_oct2.reverse()
y_oct2.reverse()

for i in range(len(x_quad1_new)):
    x_quad1.append(x_oct2[i])
    y_quad1.append(y_oct2[i])
    
x_quad2_new = [(x_cent - x) for x in x_quad1_new]
y_quad2_new = [(y_cent + y) for y in y_quad1_new]

x_quad3_new = [(x_cent - x) for x in x_quad1_new]
y_quad3_new = [(y_cent - y) for y in y_quad1_new]

x_quad4_new = [(x_cent + x) for x in x_quad1_new]
y_quad4_new = [(y_cent - y) for y in y_quad1_new]

x_quad1_new = [(x_cent + x) for x in x_quad1_new]
y_quad1_new= [(y_cent + y) for y in y_quad1_new]

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(
    # x_quad1, y_quad1, x_quad2, y_quad2, x_quad3, y_quad3, x_quad4, y_quad4,
    x_quad1_new, y_quad1_new, x_quad2_new, y_quad2_new, x_quad3_new, y_quad3_new, x_quad4_new, y_quad4_new
)
ax.set_aspect('equal', adjustable='box')
plt.title("Bresenham Circle Drawing Algorithm")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()



# T=[[1, 0, x_trans],
#    [0, 1, y_trans],
#    [0, 0, 1]]

# R=[0, 0, 0]

            
# for i in range(len(X)):
#     B=[X[i],Y[i],1]
#     R=np.dot(T,B)
#     X_new.append(R[0])
#     Y_new.append(R[1])
    
    
    
# X_new
# Y_new


# fig = plt.figure()
# ax = fig.add_subplot(111)

# plt.plot(X,Y,X_new,Y_new)
# plt.show()