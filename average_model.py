# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:32:48 2018

@author: drxkm
"""
import csv 
import numpy as np
import pandas as pd
from pandas import ExcelWriter
import matplotlib.pyplot as plt
import pylab as pl


MAXLEN=261003
flag=10
mean = np.zeros((MAXLEN,1))

#%%
correlation = np.zeros((MAXLEN,539))
correlation_return = csv.reader(open('./data/correlation.csv','r'))    #两个合并之后
next(correlation_return)
i=0
for line in correlation_return:
    correlation[i,:]=line[1:]
    i=i+1
    if(i%10000==0):
        print(i)
    if (i == MAXLEN):
        break

for i in range(0,MAXLEN):
    for j in range (0,flag):        #range(0,5) 打印0,1,2,3,4
        tempmax = np.argmax(correlation[i])
        correlation[i][tempmax]=0
        tempmin = np.argmin(correlation[i])
        correlation[i][tempmin]=0
    mean[i]=sum(correlation[i])/(539-2*flag)
    if(i%10000==0):
        print(i)
    
PDcorrelation = pd.DataFrame(mean)
PDcorrelation.to_csv('mean_1026.csv')
