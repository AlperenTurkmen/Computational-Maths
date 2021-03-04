import matplotlib.pyplot as plt
import numpy as np
# Alperen Türkmen 700051535

def euler_method(step_size):
    '''
    This function here takes the parameter of:

    :param step_size: is the step size to approximate.

    It approximates the function according to previous y values and its increase rate.
    (Euler's method)
    It also invokes the exact graph function.
    '''
    t = np.linspace(0, 6, step_size + 1)
    y0 = -3 #c for this particular function.
    f = lambda y, x: (x + (y / 5)) #The given function
    y = np.zeros(len(t))
    y[0] = y0
    for n in range(0, len(t) - 1):
        y[n + 1] = y[n] + f(y[n], t[n]) * (t[n + 1] - t[n]) #It applies the euler's method here, as given in the lectures.

    plt.plot(t, y, 'b.-')
    plt.grid()
    exact_results()


def exact_results():
    '''
    It draws the graph of the exact graph according to the integral of the given equation.
    :return:
    '''
    x1 = np.arange(0, 5, 0.01)
    c = -3
    y1 = ((x1 ** 2) / 2) + c #The term in the middle is gone because it's zero.
    plt.plot(x1, y1, 'r-')
    plt.legend(['Euler', 'Exact']) #This creates legends for graphs.


plt.subplot(1, 3, 1)
plt.title("Step size: 1")
euler_method(5)

plt.subplot(1, 3, 2)
plt.title("Step size: 0.2")
euler_method(25)

plt.subplot(1, 3, 3)
plt.title("Step size: 0.05")
euler_method(100)

plt.show()