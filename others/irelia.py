from math import floor
import matplotlib.pyplot as plt
import numpy as np

#calculates damage by blade of the ruined king passive.
x=[2000]

for i in range(0,20):

    z=x[i]-0.12*x[i]
    int(floor(z))
    x.append(z)
# print (x)


x_axis= np.arange(0,2000,200).tolist()

y_axis= list(range(0,21,1))
y_axis.reverse()

print( x_axis,"\n",y_axis)


plt.plot(x_axis,y_axis)
plt.figure()


plt.xlabel("Number of physical attacks by blade of ruined king")
plt.ylabel("Health of enemy marksman")

plt.plot(y_axis,x)