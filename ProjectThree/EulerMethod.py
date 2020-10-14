# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171

import numpy as np
import matplotlib.pyplot as plt

def odeEulerOne(fx,x0,t):

    '''Approximate the solution of y'=f(y,t) by Euler's method.

    Parameters
    ----------
    fx : function
        Right-hand side of a differential equation y'=f(t,y), y(t_0)=y_0
    y0: number
        Initial value y(t0)=y0 where t0 is the entry at index 0 in the array t
    t : array
        1D NumPy array of t values where we approximate y values. Time step
        at each iteration is given by t[n+1] - t[n].

    Returns
    -------
    y : 1D NumPy array
        Approximation y[n] of the solution y(t_n) computed by Euler's method.
    '''

    def Method(f, New0,t2):
        Next = np.zeros(len(t2))
        Next[0] = New0
        for n in range(0,len(t2)-1):
            Next[n+1] = Next[n] + f(Next[n],t2[n])*(t2[n+1] - t2[n])
        return Next

    
    x=Method(f=fx, New0=x0, t2=t)

    return x



def odeEulerTwo(R0=0, F0=0, alpha=1, beta=1, gamma=1, delta=1, t=[]):


    # Solve Lotka-Volterra equations
    # Euler method.
    # x0 and y0 are the inputs of my cordinates
    #alpha, beta, gamma, delta are the constants of the System Lotka-Volterra
    #  t is an input and 1D NumPy array of t values where we approximate y values. 
    #    Time step at each iteration is given by t[n+1] - t[n].

    R = np.zeros(len(t)) # Pre-allocate the memory for R
    F = np.zeros(len(t)) # Pre-allocate the memory for F

    R[0] = R0
    F[0] = F0

    for n in range(0,len(t)-1):
        dt = t[n+1] - t[n]
        R[n+1] = R[n]*(1 + alpha*dt - gamma*dt*F[n])
        F[n+1] = F[n]*(1 - beta*dt + delta*dt*R[n])
    return R,F


