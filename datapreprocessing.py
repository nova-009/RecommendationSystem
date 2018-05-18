#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 18:40:31 2018


!!!Do not run more than once,appends files!!!


@author: pallavi
"""

import pandas as pd
import numpy as np


           
header = ['user_id', 'movie_id', 'rating','timestamp']
train_data = pd.read_csv('data/ml-100k/ua.base', sep='\t', names=header)
train_data=train_data.drop(['timestamp'],axis=1)
test_data = pd.read_csv('data/ml-100k/ua.test', sep='\t', names=header)
test_data=test_data.drop(['timestamp'],axis=1)
 
header=['movie_id' , 'movie_title' , 'release_date', 'video_release_date' ,'IMDb_URL' , 'unknown' , 'Action' , 'Adventure' , 'Animation' ,'Children', 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,'Thriller' , 'War' , 'Western']

movie_data= pd.read_csv('data/ml-100k/u.item', sep='|', names=header)
movie_data=movie_data[['movie_id' ,'Action' , 'Adventure' , 'Animation' ,'Children', 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,'Thriller' , 'War' , 'Western']]


train_data=train_data.join(movie_data.set_index('movie_id'), on='movie_id')
train_data=train_data.drop(['movie_id'],axis=1)

test_data=test_data.join(movie_data.set_index('movie_id'), on='movie_id')
test_data=test_data.drop(['movie_id'],axis=1)


header = ['user_id','Action' , 'Adventure' , 'Animation' ,
              'Children', 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,
              'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,
              'Thriller' , 'War' , 'Western']

avg_rating = pd.read_csv('data/avg_ratings.txt', sep='\t', names=header)
avg_rating=np.array(avg_rating)


for i in range(3):
    user_ids=open('data/cluster_info/users_under_cluster'+str(i)+'.txt').read().split('\n')
    user_ids.remove('')
    for u in user_ids:
        df=train_data[train_data['user_id']==int(u)]
        rating=df['rating']
        df=df.drop(['rating'],axis=1)
        df=df.join(rating)
        df=np.array(df)
        avg_rating[int(u)-1][0]=1
        avg=np.append(avg_rating[int(u)-1],[1])
        df=avg*df
        df=pd.DataFrame(df)
        rating=df[19]
        df=df.drop([19],axis=1)
        df.to_csv("data/train/cluster"+str(i)+"_X_train.txt", header=None, index=None, sep='\t', mode='a')
        rating.to_csv("data/train/cluster"+str(i)+"_Y_train.txt", header=None, index=None, sep='\t', mode='a')
        
        df=test_data[test_data['user_id']==int(u)]
        rating=df['rating']
        df=df.drop(['rating'],axis=1)
        df=df.join(rating)
        df=np.array(df)
        avg_rating[int(u)-1][0]=1
        avg=np.append(avg_rating[int(u)-1],[1])
        df=avg*df
        df=pd.DataFrame(df)
        rating=df[19]
        df=df.drop([19],axis=1)
        df.to_csv("data/test/cluster"+str(i)+"_X_test.txt", header=None, index=None, sep='\t', mode='a')
        rating.to_csv("data/test/cluster"+str(i)+"_Y_test.txt", header=None, index=None, sep='\t', mode='a')
