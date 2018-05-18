#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 07:40:42 2018

@author: pallavi
"""
import pickle
import pandas as pd
import numpy as np
"""
header = ['user_id','Action' , 'Adventure' , 'Animation' ,
              'Children', 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,
              'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,
              'Thriller' , 'War' , 'Western']

avg_rating = pd.read_csv('data/avg_ratings.txt', sep='\t', names=header)
avg_rating=avg_rating.drop('user_id',axis=1)
avg_rating=np.array(avg_rating)

header=['movie_id' , 'movie_title' , 'release_date', 'video_release_date' ,'IMDb_URL' , 'unknown' , 'Action' , 'Adventure' , 'Animation' ,'Children', 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,'Thriller' , 'War' , 'Western']
movie_data= pd.read_csv('data/ml-100k/u.item', sep='|', names=header)
movie_data=movie_data[['Action' , 'Adventure' , 'Animation' ,'Children', 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,'Thriller' , 'War' , 'Western']]

movie_data=np.array(movie_data)

for i in range(612,943):
    m=avg_rating[i]*movie_data
    m=pd.DataFrame(m)
    m.to_csv('data/all/'+str(i+1)+'.txt',header=None, index=None, sep='\t', mode='w')
    


"""
labels_unpickle = open('labels.pkl', 'rb')
labels = pickle.load(labels_unpickle) 

user_id=int(input('Enter user id:'))

cluster_id=labels[user_id-1]


model_unpickle = open('saved_objects/model_'+str(cluster_id)+'.pkl', 'rb')
mlpRegressor = pickle.load(model_unpickle)

X=pd.read_csv('data/all/'+str(user_id)+'.txt', sep='\t')
X=np.array(X)

Y_pred=mlpRegressor.predict(X)


top5=Y_pred.argsort()[-5:][::-1]    
    
header=['movie_id' , 'movie_title' , 'release_date', 'video_release_date' ,'IMDb_URL' , 'unknown' , 'Action' , 'Adventure' , 'Animation' ,'Children', 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,'Thriller' , 'War' , 'Western']
movie_data= pd.read_csv('data/ml-100k/u.item', sep='|', names=header)

print('Top 5 recommended movies are:')
for i in top5:
    x=movie_data[movie_data['movie_id']==i+1]
    x=np.array(x)
    print(str(x[0][1])+'\t'+str(Y_pred[i]))

