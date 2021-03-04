import matplotlib.pyplot as plt
import numpy as np
# Alperen Türkmen 700051535

# Points arrays
xpoints = []
ypoints = []
xpoints_induced = []
ypoints_induced = []
# Default Values
a = 4
b = 3
matrix_A = np.multiply(1 / b,np.array([[b, 1], [-1, 1]]))#Top row first, bottom row second.


def inducedby (xpoints, ypoints,xpoints_induced,ypoints_induced) :
    '''
    This function here takes parameters of:

    xpoints: X values of the coordinates of points. Type:List
    ypoints: Y values of the coordinates of points. Type:List
    xpoints_induced: An array to store the induced points' X values. Type:List
    ypoints_induced: An array to store the induced points' X values. Type:List

    It simply takes the points to be induced, matrix_A was already declared,
    And all this function should do is: multiply them.
    Then of course store that values in empty arrays.
    '''
    xpoints_induced.clear() # I cleared them everytime because otherwise it will come full, we don't want it.
    ypoints_induced.clear()
    for i in range(len(xpoints)): #It iterates the xpoints array
        x = xpoints[i]
        y = ypoints[i]
        p = np.array([x, y])
        p2 = np.matmul( matrix_A,p )# If we do p x matrix_A, it will rotate the figure to the left.
        xpoints_induced.append(p2[0])
        ypoints_induced.append(p2[1])


def transformed_figure(a) :
    '''
    This function here takes parameter of:

    a: this is the variable which was described in the coursework sheet.

    It has 5 parts, 1 for each part except the 4th (It has 2 parts because of 'then').
    We take the coordinates, split them into x's and y's, assign these arrays into
    an array named 'xpoints' and 'ypoints'. And then, we should draw this raw figure on a canvas.
    '''
    #part1
    xpoints = np.array([a, a, -a, -a, a])
    ypoints = np.array([a, -a, -a, a, a])
    inducedby(xpoints,ypoints,xpoints_induced,ypoints_induced)
    plt.plot(xpoints_induced, ypoints_induced)
    # part2
    xpoints = np.array([1 - a, -a / 4, -a / 4, 1 - a, 1 - a])
    ypoints = np.array([a - 1, a - 1, a / 2, a / 2, a - 1])
    inducedby(xpoints, ypoints, xpoints_induced, ypoints_induced)
    plt.plot(xpoints_induced, ypoints_induced)
    # part3
    xpoints = np.array([a / 4, a - 1])
    ypoints = np.array([a - 1, a / 2])
    inducedby(xpoints, ypoints, xpoints_induced, ypoints_induced)
    plt.plot(xpoints_induced, ypoints_induced)
    # then
    xpoints = np.array([a - 1, a / 4])
    ypoints = np.array([a - 1, a / 2])
    inducedby(xpoints, ypoints, xpoints_induced, ypoints_induced)
    plt.plot(xpoints_induced, ypoints_induced)
    # part4
    xpoints = np.array([a - 1, a - 1, 1 - a, 1 - a])
    ypoints = np.array([-a / 4, -a / 2, -a / 2, -a / 4])
    inducedby(xpoints, ypoints, xpoints_induced, ypoints_induced)
    plt.plot(xpoints_induced, ypoints_induced)


def figure (a) :
    '''This function here takes parameter of:
        a: this is the variable which was described in the coursework sheet.

        It has 5 parts, 1 for each part except the 4th (It has 2 parts because of 'then').
        We take the coordinates, split them into x's and y's, assign these arrays into
        an array named 'xpoints' and 'ypoints'. And then, We should draw this transformed figure.
        '''
    # part1
    xpoints = np.array([a, a, -a, -a, a])
    ypoints = np.array([a, -a, -a, a, a])
    plt.plot(xpoints, ypoints)
    # part2
    xpoints = np.array([1 - a, -a / 4, -a / 4, 1-a,1 - a])
    ypoints = np.array([ a-1, a-1 , a/2, a/2, a-1])
    plt.plot(xpoints, ypoints)
    # part3
    xpoints = np.array([a/4, a-1])
    ypoints = np.array([a-1, a/2])
    plt.plot(xpoints, ypoints)
    # then
    xpoints = np.array([a-1, a / 4])
    ypoints = np.array([a - 1, a / 2])
    plt.plot(xpoints, ypoints)
    # part4
    xpoints = np.array([a-1, a-1, 1-a, 1 - a])
    ypoints = np.array([-a/4, -a/2,-a / 2, -a / 4])
    plt.plot(xpoints, ypoints)

def main() :
    '''
    This is my main function, it creates subplots, titles,
    :return:
    '''
    #Figure
    plt.subplot(1, 2, 1)
    plt.title("Figure")
    figure(a) #This will invoke the function that I defined before.
    # transformed points Induced by matrix
    plt.subplot(1, 2, 2)
    plt.title("Transformed Figure")
    transformed_figure(a) #This will also invoke the function I defined before.
    #show all
    plt.show() # Show the canvas.

if __name__ == "__main__":
    main()
