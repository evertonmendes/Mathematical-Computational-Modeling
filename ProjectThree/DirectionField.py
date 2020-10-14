# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171

import numpy as np
import matplotlib.pyplot as plt


def Direction_Field(f, Ode_type='1', xran=[], yran=[]):

    
    


    if Ode_type=='2':


        """
        Plot the direction field for an ODE written in the form 
            x' = F(x,y)
            y' = G(x,y)
        
        The functions F,G are defined in the list of strings f.
        
        Input
        -----
        f:    list of strings ["F(X,Y)", "G(X,Y)"
            F,G are functions of X and Y (capitals).
        xran: list [xmin, xmax] (optional)
        yran: list [ymin, ymax] (optional)
        grid: list [npoints_x, npoints_y] (optional)
            Defines the number of points in the x-y grid.
        color: string (optional)
            Color for the vector field (as color defined in matplotlib)
        """


        grid=[21,21]
        x = np.linspace(xran[0], xran[1], grid[0])
        y = np.linspace(yran[0], yran[1], grid[1])
        def dX_dt(X, Y, t=0): return map(eval, f)
        
        X , Y  = np.meshgrid(x, y)  # create a grid
        DX, DY = dX_dt(X, Y)        # compute growth rate on the grid
        M = (np.hypot(DX, DY))      # Norm of the growth rate 
        M[ M == 0] = 1.             # Avoid zero division errors 
        DX = DX/M                   # Normalize each arrows
        DY = DY/M  

        return X,Y, DX, DY,M

    if Ode_type=='1':


        x = np.linspace(xran[0],xran[1],20)
        y = np.linspace(yran[0],yran[1],20)

        
        listDomain=[]
        listfun=[]

        # use x,y
        for j in x:
            for k in y:
                slope = f(k,j)
                domain = np.linspace(j-0.07,j+0.07,2)
                def fun(x1,y1):
                    z = slope*(domain-x1)+y1
                    return z

                listDomain.append(domain)
                listfun.append(fun(j,k))
                #plt.plot(domain,fun(j,k),solid_capstyle='projecting',solid_joinstyle='bevel')


        return listDomain, listfun
