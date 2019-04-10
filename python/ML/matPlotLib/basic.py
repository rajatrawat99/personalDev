import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
x = np.linspace(0,5,10)
y = x ** 2
print("x is",x)
print("y is",y)

#Functional method
plt.plot(x,y)
plt.title("Graph 1. Simple Graph")
plt.show()

plt.plot(x,y,'-r') #'-r' to make in red color
plt.title("Graph 2. in red color")
plt.show()

plt.plot(x,y)
plt.xlabel("this is x label")
plt.ylabel("this is y label")
plt.title("Graph 3. with labels")
plt.show()

plt.subplot(1,2,1) #(no of rows, no of colums, graph no)
plt.plot(x,y,"r")
plt.subplot(1,2,2)
plt.plot(y,x,"b")
plt.show()
