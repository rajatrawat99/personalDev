#object oriented approach
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,10)
y = x ** 2

def example1():
    fig = plt.figure()
    axes = fig.add_axes([.1,.1,.8,.8])
    axes.set_xlabel("X Label")
    axes.set_ylabel("Y Label")
    axes.set_title("Object graph")
    axes.plot(x,y)
    plt.show()

def example2():
    fig = plt.figure()
    axes1 = fig.add_axes([.1,.1,.8,.8])
    axes2 = fig.add_axes([.2,.5,.2,.2])
    axes1.plot(x,y)
    axes1.set_title("large graph")
    axes2.plot(x,y)
    axes1.set_title("small graph")
    plt.show()




choice = int(input("example 1 or example 2: "))

print(choice)
if choice == 1:
    example1()
elif choice == 2:
    example2()
