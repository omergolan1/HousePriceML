"""
File   :  MLalgoHousePrice.py
Author :  Omer Golan & Omer Shtresler
Date   :  19/12/2020
Class  :  Yod-3
This file contains the class "MLalgoHousePrice" which is responsible for the Machine-Learning  part of the project.
in this class we organize the the data, train the machine and test it.
"""
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import linear_model


class MLalgoHousePrice(object):

    def __init__(self):
        """
        the function organize the data and trains the machine.
        args:
        output:
        """
        self.df_train = pd.read_csv("train.csv")
        self.mylistSaleprice = ['MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'HouseStyle', 'YrSold',
                                'OverallCond',
                                'SalePrice', 'YearBuilt', 'YearRemodAdd', 'OverallQual', 'BedroomAbvGr', '1stFlrSF',
                                '2ndFlrSF'
            , 'TotalBsmtSF', 'FullBath']

        self.mylist = ['MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'HouseStyle', 'YrSold', 'OverallCond',
                       'YearBuilt',
                       'YearRemodAdd', 'OverallQual', 'BedroomAbvGr', '1stFlrSF', '2ndFlrSF', 'TotalBsmtSF', 'FullBath']

        self.dfc = self.df_train[self.mylistSaleprice]

        # changes the data into int values so we could use the fit function later
        self.dfc.loc[self.dfc['MSZoning'] == 'A', 'MSZoning'] = 1
        self.dfc.loc[self.dfc['MSZoning'] == 'C', 'MSZoning'] = 2
        self.dfc.loc[self.dfc['MSZoning'] == 'FV', 'MSZoning'] = 3
        self.dfc.loc[self.dfc['MSZoning'] == 'I', 'MSZoning'] = 4
        self.dfc.loc[self.dfc['MSZoning'] == 'RH', 'MSZoning'] = 5
        self.dfc.loc[self.dfc['MSZoning'] == 'RL', 'MSZoning'] = 6
        self.dfc.loc[self.dfc['MSZoning'] == 'RP', 'MSZoning'] = 7
        self.dfc.loc[self.dfc['MSZoning'] == 'RM', 'MSZoning'] = 8
        self.dfc.loc[self.dfc['MSZoning'] == 'C (all)', 'MSZoning'] = 9

        self.dfc.loc[self.dfc['HouseStyle'] == '1Story', 'HouseStyle'] = 1
        self.dfc.loc[self.dfc['HouseStyle'] == '2Story', 'HouseStyle'] = 2
        self.dfc.loc[self.dfc['HouseStyle'] == '1.5Fin', 'HouseStyle'] = 3
        self.dfc.loc[self.dfc['HouseStyle'] == '1.5Unf', 'HouseStyle'] = 4
        self.dfc.loc[self.dfc['HouseStyle'] == 'SFoyer', 'HouseStyle'] = 5
        self.dfc.loc[self.dfc['HouseStyle'] == 'SLvl', 'HouseStyle'] = 6
        self.dfc.loc[self.dfc['HouseStyle'] == '2.5Unf', 'HouseStyle'] = 7
        self.dfc.loc[self.dfc['HouseStyle'] == '2.5Fin', 'HouseStyle'] = 8

        self.dfc["LotFrontage"].fillna(0, inplace=True)
        self.dfc.fillna(0)

        # splits the the data into train data and test data
        self.msk = np.random.rand(len(self.dfc)) < 0.8
        self.train = self.dfc[self.msk]
        self.test = self.dfc[~self.msk]

        self.regr = linear_model.LinearRegression()
        x = np.asanyarray(self.train[self.mylist])
        y = np.asanyarray(self.train[['SalePrice']])
        self.regr.fit(x, y)

        # The coefficients
        # print('Coefficients: ', self.regr.coef_)
        # print('Intercept: ', self.regr.intercept_)

    def GetError(self):
        """
        the function calculates the accuracy of the machine
        args:
        :return: the machine error value in precentege
        """
        self.y_hat = self.regr.predict(self.test[self.mylist])

        x = np.asanyarray(self.test[self.mylist])
        y = np.asanyarray(self.test[['SalePrice']])

        # print('Variance score: %.2f' % self.regr.score(x, y))
        return self.regr.score(x, y)

    def predict(self, argsList):
        """
        the function calculates the value of an house based on "argsList"
        :param argsList: array that contains the input of the user - the parameters for the house
        :return: (2d array) the value of the house based on the parameters
        """
        return self.regr.predict([argsList]) - 20000
