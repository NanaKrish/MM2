def f(x,y):
  return x**2+y**2

def get_k1(xi,yi):
  return f(xi, yi)

def get_yi_plus_1(xi, yi, h):
  k1 = h*get_k1(xi, yi)
  k2 = h*f(xi + (h/2), yi + (k1/2))
  k3 = h*f(xi + (h/2), yi + (k2/2))
  k4 = h*f(xi + h, yi+k3)
  print(k1,k2,k3,k4)
  return yi + (1/6*(k1 + 2*k2 + 2*k3 + k4))

print(get_yi_plus_1(1,1.2,0.05))


# Python program to implement Runge Kutta method
# A sample differential equation "dy / dx = (x - y)/2"

def dydx(x, y):

    return ((x - y)/2)
 
# Finds value of y for a given x using step size h
# and initial value y0 at x0.

def rungeKutta(x0, y0, x, h):

    # Count number of iterations using step size or

    # step height h

    n = (int)((x - x0)/h) 

    # Iterate for number of iterations

    y = y0

    for i in range(1, n + 1):

        "Apply Runge Kutta Formulas to find next value of y"

        k1 = h * dydx(x0, y)

        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)

        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)

        k4 = h * dydx(x0 + h, y + k3)
 

        # Update next value of y

        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
 

        # Update next value of x

        x0 = x0 + h

    return y
 
# Driver method

x0 = 0

y = 1

x = 2

h = 0.2

print ('The value of y at x is:', rungeKutta(x0, y, x, h))
 
# This code is contributed by Prateek Bhindwar
