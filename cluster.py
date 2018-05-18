#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 08:10:43 2018

@author: pallavi
"""
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pickle

#reduce dimentionality

header = ['user_id','Action' , 'Adventure' , 'Animation' ,
              'Children', 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,
              'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,
              'Thriller' , 'War' , 'Western']

avg_rating = pd.read_csv('data/normalized_avg_ratings.txt', sep='\t', names=header)
avg_rating=avg_rating.drop(['user_id'],axis=1)

#principal component analysis 
pca = PCA(n_components=5)
avg_rating=pca.fit_transform(avg_rating)

kmeans = KMeans(n_clusters=3, random_state=0).fit(avg_rating)
labels=kmeans.labels_

"""

for i in range(943):
    f=open("data/cluster_info/users_under_cluster"+str(labels[i])+".txt","a")
    f.write(str(i)+"\n")
    f.close
"""


    
labels_pickle = open('labels.pkl', 'wb')
pickle.dump(labels, labels_pickle)
labels_pickle.close()

