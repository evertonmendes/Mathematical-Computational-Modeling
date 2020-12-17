# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171

import matplotlib.pyplot as plt
import numpy as np

def PlotGenetic(data, dataD):

    t=np.linspace(0, len(data), len(data))


    plt.title('Shortest Distances')
    plt.xlabel('generations')
    plt.ylabel('minimum distance')
    plt.errorbar(t, data, dataD, ecolor='gray', color='red')
    plt.show()


