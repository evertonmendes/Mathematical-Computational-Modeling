# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171

import numpy as np


#function that aplies LLS method to fitting surfaces in multidimensional data
def LLS(samplesX=[], samplesY=[], samplesZ=[], errorfunction='linear'):

    p=[]
    A=[]
    Y1=[]


    #-------- TWO FEATURES ---------
    
    if(errorfunction ==('linear') or ('quadratic') or ('cubic')):
        for i in range(len(samplesY)):
            Y1.append([samplesY[i]])
            
    
    if (errorfunction=='linear'):
        for i in range(len(samplesX)):
            A.append([1,samplesX[i]])

    if (errorfunction=='quadratic'):
        for i in range(len(samplesX)):
            A.append([1, samplesX[i], (samplesX[i])**2])
            
    if (errorfunction=='cubic'):
        for i in range(len(samplesX)):
            A.append([1, samplesX[i], (samplesX[i])**2, (samplesX[i])**3])


    #-------- THREE FEATURES --------

    if(errorfunction == ('surfacePlane' or 'surfaceQuadratic')):
        Y1=[]
        for i in range(len(samplesZ)):
            Y1.append((samplesZ[i]))

        
    if(errorfunction=='surfacePlane'):
        for i in range(len(samplesX)):
            A.append([1, samplesX[i], samplesY[i]])


    if(errorfunction=='surfaceQuadratic'):
        A=[]
        for i in range(len(samplesX)):
            A.append([1, samplesX[i], samplesY[i], (samplesX[i])*(samplesY[i]), (samplesX[i])**2, (samplesY[i])**2])
            
    

    #do the necessary operations to obtain the coeficients of the methods

    A=np.matrix(A)
    Y1=np.matrix(Y1)
    if(errorfunction=='surfacePlane'):
        Y1=Y1.transpose()
    P=np.matrix(p)
    S=np.matmul((A.transpose()), A)
    #print((np.matmul(np.linalg.inv(S), A.transpose())).shape)
    P=np.matmul((np.matmul(np.linalg.inv(S), A.transpose())), Y1)
    P=P.getA1()
    
    #print(P)
        
    return P
