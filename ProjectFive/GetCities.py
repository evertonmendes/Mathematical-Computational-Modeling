# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171

from random import randint
import matplotlib.pyplot as plt





#cria um conjunto de n pontos aleatórios dentro de um circulo de raio dado
def Points(n, radius):

    pontos=[]
    while (len(pontos)<n):

        x=0.00001*randint((-1)*radius*100000,radius*100000)
        y=0.00001*randint((-1)*radius*100000,radius*100000)
        
        dist=((x**2)+(y**2))**0.5
        if dist<radius:

            pontos.append([x, y])



    return pontos



#Plota os pontos 
def Grafics(lista):


    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cidades')
    plt.axis([-1.1,1.1,-1.1,1.1])

        
    x=[]
    y=[]
    for i in range(len(lista)):
        x.append(lista[i][0])
        y.append(lista[i][1])
    
    
    
    for i in range(len(lista)):
        plt.plot(x, y,'.',  color='blue')

    plt.show()



points=Points(15, 1)
Grafics(points)


f = open("cities.txt", "a")
for i in points:

    f.write(str(i[0])+' '+str(i[1])+'\n')

f.close()