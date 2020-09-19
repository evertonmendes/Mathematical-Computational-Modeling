# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171

import pandas as pd
from sklearn.datasets import load_breast_cancer, load_boston, fetch_california_housing
import numpy as np


#function that imports the require Data

def GetDatasets():

    #importing Breast Cancer Data

    dataCancer, targetCancer= load_breast_cancer(return_X_y=True, as_frame=True)
    MixCancer=dataCancer.join(targetCancer)

    featureCancer=load_breast_cancer().feature_names
    featureCancer=featureCancer.tolist()
    featureCancer.append('target')

    #MixCancer - Panda Dataframe of the Data
    #featureCancer - an array with the feature names of the samples


    '''---------------------------------------'''


    #importing Boston Housse-Prices Data

    dataBoston, targetBoston=load_boston(return_X_y=True)
    

    feature_names=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
    df1=pd.DataFrame(dataBoston, columns=feature_names)
    df2=pd.DataFrame(targetBoston, columns=['MEDV'])

    MixBoston=df1.join(df2)
    feature_names.append('MEDV')

    #MixBoston - Panda Dataframe of the Data
    #feature_names - an array with the features of the samples


    '''---------------------------------------'''

    #importing California Housing Data

    dataCalifornia, targetCalifornia=fetch_california_housing(return_X_y=True, as_frame=True)
    MixCalifornia=dataCalifornia.join(targetCalifornia)

    featureCalifornia=fetch_california_housing().feature_names
    featureCalifornia.append('MedHouseVal')

    #MixCalifornia - Panda Dataframe of the data
    #featureCalifornia - an array with the features of the set



    return [MixBoston, feature_names],[MixCancer, featureCancer],[MixCalifornia, featureCalifornia]




#-----------------------------------

