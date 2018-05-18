#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 08:10:43 2018

@author: pallavi
"""
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


#reduce dimentionality

header = ['Action' , 'Adventure' , 'Animation' ,
              'Children', 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,
              'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,
              'Thriller' , 'War' , 'Western']

avg_rating = pd.read_csv('data/normalized_avg_ratings.txt', sep='\t', names=header)

a_mean_var=[]
attributes=[]
for i in range(1,19):
    attributes.append(i)
for i in range(1,19):
    x=np.array(avg_rating)
    n_users=x.shape[0]
    
    pca=PCA(i)
    p=pca.fit_transform(x)
    variance=[]
    
    for j in range(n_users):
        p_array=p[j]
        var=np.var(p_array)
        variance.append(var)
        
    mean_var_i=np.mean(variance)
    a_mean_var.append(mean_var_i)
   
    
plt.plot(attributes,a_mean_var, label='rating')

leg = plt.legend(loc='best', ncol=1)
leg.get_frame().set_alpha(0.5)


plt.xlabel('attributes')
plt.ylabel('variance')
plt.show()



    
"""    
preference = pd.read_csv('data/preference.txt', sep='\t', names=header)

p_mean_var=[]

for i in range(1,19):
    x=np.array(preference)
    n_users=x.shape[0]
    
    pca=PCA(i)
    p=pca.fit_transform(x)
    variance=[]
    
    for j in range(n_users):
        p_array=p[j]
        var=np.var(p_array)
        variance.append(var)
        
    mean_var_i=np.mean(variance)
    p_mean_var.append(mean_var_i)

ratio = pd.read_csv('data/consumptionRatio.txt', sep='\t', names=header)

r_mean_var=[]

for i in range(1,19):
    x=np.array(ratio)
    n_users=x.shape[0]
    
    pca=PCA(i)
    p=pca.fit_transform(x)
    variance=[]
    
    for j in range(n_users):
        p_array=p[j]
        var=np.var(p_array)
        variance.append(var)
        
    mean_var_i=np.mean(variance)
    r_mean_var.append(mean_var_i)  
   

plt.plot(attributes,a_mean_var, label='rating')

plt.plot(attributes,r_mean_var,label='ratio')

plt.plot(attributes,p_mean_var,label='preference')

leg = plt.legend(loc='best', ncol=1)
leg.get_frame().set_alpha(0.5)


plt.xlabel('attributes')
plt.ylabel('variance')
plt.show()
""" 