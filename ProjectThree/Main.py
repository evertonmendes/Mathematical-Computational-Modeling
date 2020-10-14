# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171

import numpy as np
import matplotlib.pyplot as plt
import math
from DirectionField import Direction_Field
from EulerMethod  import odeEulerOne,odeEulerTwo
from Plot import Plot_Dif_Eq




#creating the model of each ODE's or ODE's System

malt=lambda y,t: y

Malthusian=Plot_Dif_Eq(f1=malt, xrange=[-3, 3], yrange=[-3,3], Equation='1')
Malthusian.PlotDirection()
Malthusian.PlotEulerMethod()



logist=lambda y,t: y*(1-y)
logistic= Plot_Dif_Eq(f1=logist, xrange=[-3,3], yrange=[-3,3], Equation='1')
logistic=PlotDirection()
logistic.PlotEulerMethod()


lotka = ["X - X*Y", "X*Y - Y"]
Lotka_Volterra=Plot_Dif_Eq(f1=lotka, xrange=[-3,3], yrange=[-3,3], Equation='2')
Lotka_Volterra.PlotDirection()
Lotka_Volterra.PlotEulerMethod()


