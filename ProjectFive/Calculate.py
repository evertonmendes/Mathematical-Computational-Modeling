# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171


#Calculate de Average of the elements in an array
def Average(lista=[]):

        soma=0
        for i in range(len(lista)):
            soma+=lista[i]

        return (soma/(len(lista)))

#Calculate de Stardard Deviation of the elements in an array
def StandardDeviation(lista=[]):

        soma=0
        for i in range(len(lista)):
            soma+=(lista[i]-(Average(lista)))**2

        return ((soma/(len(lista)-1))**0.5)