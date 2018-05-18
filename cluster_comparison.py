#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 08:10:43 2018

@author: pallavi
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

#reduce dimentionality

header = ['user_id','Action' , 'Adventure' , 'Animation' ,
              'Children', 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,
              'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,
              'Thriller' , 'War' , 'Western']

avg_rating = pd.read_csv('data/avg_ratings.txt', sep='\t', names=header)
avg_rating=avg_rating.drop(['user_id'],axis=1)
a_itertia=[]
clusters=[]

pca = PCA(n_components=5)
avg_rating=pca.fit_transform(avg_rating)

for i in range(1,19):
    clusters.append(i)
    
for i in range(1,19):
    x=np.array(avg_rating)
    kmeans = KMeans(n_clusters=i, random_state=0).fit(x)
    a_itertia.append(kmeans.inertia_)
   


header1 = ['Action' , 'Adventure' , 'Animation' ,
              'Children', 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,
              'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,
              'Thriller' , 'War' , 'Western']    
 
preference = pd.read_csv('data/preference.txt', sep='\t', names=header1)

p_itertia=[]
clusters=[]

pca = PCA(n_components=5)
preference=pca.fit_transform(preference)

for i in range(1,19):
    clusters.append(i)
    
for i in range(1,19):
    x=np.array(preference)
    kmeans = KMeans(n_clusters=i, random_state=0).fit(x)
    p_itertia.append(kmeans.inertia_)

ratio = pd.read_csv('data/consumptionRatio.txt', sep='\t', names=header)
ratio=ratio.drop(['user_id'],axis=1)
r_itertia=[]
clusters=[]

pca = PCA(n_components=5)
ratio=pca.fit_transform(ratio)


for i in range(1,19):
    clusters.append(i)
    
for i in range(1,19):
    x=np.array(ratio)
    kmeans = KMeans(n_clusters=i, random_state=0).fit(x)
    r_itertia.append(kmeans.inertia_) 
   

plt.plot(clusters,a_itertia, label='rating')
plt.plot(clusters,r_itertia,label='ratio')
plt.plot(clusters,p_itertia,label='preference')
leg = plt.legend(loc='best', ncol=1)
leg.get_frame().set_alpha(0.5)
plt.xlabel('No of clusters')
plt.ylabel('Inertia')
plt.show()

plt.plot(clusters,a_itertia, label='rating')
leg = plt.legend(loc='best', ncol=1)
leg.get_frame().set_alpha(0.5)
plt.xlabel('No of clusters')
plt.ylabel('Inertia')
plt.show()


plt.plot(clusters,r_itertia,label='ratio')
leg = plt.legend(loc='best', ncol=1)
leg.get_frame().set_alpha(0.5)
plt.xlabel('No of clusters')
plt.ylabel('Inertia')
plt.show()


plt.plot(clusters,p_itertia,label='preference')
leg = plt.legend(loc='best', ncol=1)
leg.get_frame().set_alpha(0.5)
plt.xlabel('No of clusters')
plt.ylabel('Inertia')
plt.show()