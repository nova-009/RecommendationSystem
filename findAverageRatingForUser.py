#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 00:58:07 2018

@author: pallavi
"""


import pandas as pd


header = ['user_id', 'movie_id', 'rating', 'timestamp']
rating_df = pd.read_csv('data/ml-100k/ua.base', sep='\t', names=header)

rating_df = rating_df[['user_id', 'movie_id', 'rating']]
n_users = rating_df['user_id'].max()

f=open('data/user_avg_ratings.txt','w')
for i in range(n_users):
    i_df=rating_df[rating_df['user_id']==i+1]
    num_movies=i_df.shape[0]
    line=str(i+1)
    i_ratings=i_df.as_matrix()
    del(i_df)
    
    
    
    sum_ratings=0
    for j in range(num_movies):
        rating=i_ratings[j][2]
        sum_ratings=sum_ratings+rating
    
    avg_rating=sum_ratings/num_movies
    
    f.write(str(i+1)+"\t"+str(avg_rating)+"\n") 
              
            
f.close       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        