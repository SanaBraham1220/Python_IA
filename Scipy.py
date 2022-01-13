# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 15:15:10 2022

@author: Sana Braham
"""

import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 10*np.sin(x)

a = sc.optimize.fminbound(f,# function
                          x1 = -10,# first bound 
                          x2 = 10,#second bound
                          xtol = 0.01, # Max Tolerance
                          full_output = True,# details 
                          disp = 1 ) #show only numbers

"""
print(a)
# Value of x , Value of y , 0 for convergance
# , number of iterations
(-1.3061484200406244, -7.94582288025181, 0, 11)
"""
############################""disp=2""#########################################
"""
a = sc.optimize.fminbound(f,# function
                          x1 = -10,# first bound 
                          x2 = 10,#second bound
                          xtol = 0.01, # Max Tolerance
                          full_output = True,# details 
                          disp = 2 ) #show some details

print(a)

=>Result
Optimization terminated successfully;
The returned value satisfies the termination criteria
(using xtol =  0.01 )
(-1.3061484200406244, -7.94582288025181, 0, 11)
"""
###############################################################################


############################""disp=3""######################################### 
"""
a = sc.optimize.fminbound(f,# function
                          x1 = -10,# first bound 
                          x2 = 10,#second bound
                          xtol = 0.01, # Max Tolerance
                          full_output = True,# details 
                          disp = 3 ) #show iterations

print(a)
=>Result

 Func-count     x          f(x)          Procedure
    1       -2.36068     -1.46647        initial
    2        2.36068      12.6121        golden
    3       -5.27864      36.3032        golden
    4      -0.715181     -6.04606        parabolic
    5      -0.795481     -6.50921        parabolic
    6       -1.28322     -7.94269        parabolic
    7       -1.69477     -7.05101        golden
    8       -1.29818     -7.94543        parabolic
    9       -1.30615     -7.94582        parabolic
   10       -1.30948     -7.94577        parabolic
   11       -1.30282     -7.94575        parabolic

Optimization terminated successfully;
The returned value satisfies the termination criteria
(using xtol =  0.01 )
(-1.3061484200406244, -7.94582288025181, 0, 11)
"""

###############################"other functions################################ 

def a(x):
    return (x)
def b(x):
    return (x**2)
def c(x):
    return (x**3)
def d(x):
    return (x**2 - 4*x + 1)
def e(x):
    return (x**3 + x**2 - 4*x - 3)
def f(x):
    return (1/x)

amin = sc.optimize.fminbound(a, -4, 4)
print("amin=",amin)
bmin = sc.optimize.fminbound(b, -4, 4)
print("bmin=",bmin)
cmin = sc.optimize.fminbound(c, -4, 4)
print("cmin=",cmin)
dmin = sc.optimize.fminbound(d, -4, 4)
print("dmin=",dmin)
emin = sc.optimize.fminbound(e, -4, 4)
print("emin=",emin)
fmin = sc.optimize.fminbound(f, -4, 4)
print("fmin=",fmin)

###############################################################################


def h(x):
    return x**2 + 10*np.sin(x)

x = np.arange(-10, 10, 0.1)
plt.plot(x,h(x))
plt.show()


A = sc.optimize.fmin_bfgs(h, #function
                          x0 = 50 , # a value to start
                          epsilon = 10 ,  # step
                          disp = 1 , # if 1 then display full details
                          retall = 1 ,# if 1 then display all iterations
                          maxiter = 2 ) #max no. if ierations
print(A)
####=>Result: the best solution is 35.29788524] after 3 iterations
"""
Warning: Maximum number of iterations has been exceeded.
         Current function value: 1239.195121
         Iterations: 2
         Function evaluations: 12
         Gradient evaluations: 4
(array([35.29788524]), [array([50]), array([44.95]), array([35.29788524])])
"""
###############################################################################

########################### basinhopping : the same role#######################


B = sc.optimize.basinhopping(h,  #function
                             x0 = 50 ,# a value to start
                             niter = 2 , #max no. if ierations
                             stepsize = 10 ,# step
                             disp = 0) # if 1 then display full details
print(B)

####=>Result: the best solution is -1.30644001
"""
fun: -7.9458233756152845
 lowest_optimization_result:       fun: -7.9458233756152845
 hess_inv: array([[0.0857338]])
      jac: array([1.1920929e-07])
  message: 'Optimization terminated successfully.'
     nfev: 12
      nit: 2
     njev: 4
   status: 0
  success: True
        x: array([-1.30644001])
                    message: ['requested number of basinhopping iterations completed successfully']
      minimization_failures: 0
                       nfev: 318
                        nit: 20
                       njev: 106
                          x: array([-1.30644001])

"""

############################# basinhopping :Other Function + other syntax###################
func = lambda x: np.cos(14.5 * x - 0.3) + (x + 0.2) * x
x0=[1.]

ret = sc.optimize.basinhopping(func, #function
                               x0 , # a value to start
                                # method = BFGS
                               minimizer_kwargs={"method": "BFGS"},
                               niter=200) #max no. if ierations
print("global minimum: x = %.4f, f(x0) = %.4f" % (ret.x, ret.fun))

"""
global minimum: x = -0.1951, f(x0) = -1.0009

"""
###############################################################################


def func2d(x):
    f = np.cos(14.5*x[0]-0.3)+(x[1]+0.2)*x[1]+(x[0]+0.2)*x[0]
    df = np.zeros(2)
    return f, df

x0 = [1.0, 1.0]

ret = sc.optimize.basinhopping(
        func2d,
        x0, 
        minimizer_kwargs={"method":"L-BFGS-B", "jac":True},
        niter=2000)

print("global minimum func2d: x = [%.4f, %.4f], f(x0) = %.4f" % 
      (ret.x[0],ret.x[1],ret.fun))

###############################################################################

def f(x):
    return x**2 - 2*x -15

a = sc.optimize.fsolve(f,x0 = 10 , full_output=True)
print("the equation solution:",a)

"""
## if full_output=True it show more details

(array([5.]), {'nfev': 9, 'fjac': array([[-1.]]), 'r': array([-8.00003226]), 
'qtf': array([-1.23520701e-07]), 'fvec': array([4.97379915e-13])}, 1, 
 'The solution converged.')

"""
###############################################################################


##################################Curve Fit########################################
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

#random values of X 
xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)


# y noise
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, 'b-', label='data')  # draw the blue line

popt, pcov = sc.optimize.curve_fit(func, xdata, ydata) #fitting
plt.plot(xdata, func(xdata, *popt), 'r-', #draw the red line
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))


#fit with bounds 
popt, pcov = sc.optimize.curve_fit(func,xdata,ydata,bounds=(0,[3., 1., 0.5]))
plt.plot(xdata, func(xdata, *popt),  #draw the green line
         'g--',label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()



                                                                                    