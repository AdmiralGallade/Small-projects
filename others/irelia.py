from math import floor
x=2000

for i in range(1,10):
    x=x-0.12*x
    print("Attack ", i," reduced health to " , floor(x))