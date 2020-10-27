from math import floor
import matplotlib.pyplot as plt
import numpy as np
x=2000

# for i in range(1,10):
#     x=x-0.12*x
#     print("Attack ", i," reduced health to " , floor(x))


x_axis= np.arange(0,2200,200).tolist()

y_axis= list(range(1,11,1))
y_axis.reverse()

print( x_axis,"\n",y_axis)

plt.pyplot(x_axis,y_axis)
plt.figure()

