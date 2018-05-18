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


header=['movie_id' , 'movie_title' , 'release_date', 'video_release_date' ,
              'IMDb_URL' , 'unknown' , 'Action' , 'Adventure' , 'Animation' ,
              "Children's", 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,
              'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,
              'Thriller' , 'War' , 'Western']

movie_data= pd.read_csv('data/ml-100k/u.item', sep='|', names=header)

genres=['Action' , 'Adventure' , 'Animation' ,
              "Children's", 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,
              'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,
              'Thriller' , 'War' , 'Western']

movie_data=movie_data[['movie_id' ,'Action' , 'Adventure' , 'Animation' ,
              "Children's", 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,
              'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,
              'Thriller' , 'War' , 'Western']]

n_users = rating_df['user_id'].max()
n_items = rating_df['movie_id'].max()

df=pd.DataFrame(['user_id' ,'Action' , 'Adventure' , 'Animation' ,
              'Children', 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,
              'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,
              'Thriller' , 'War' , 'Western'])
f=open('data/avg_ratings.txt','w')
for i in range(n_users):
    i_df=rating_df[rating_df['user_id']==i+1]
    num_movies=i_df.shape[0]
    line=str(i+1)
    i_ratings=i_df.as_matrix()
    del(i_df)
    
    #counts for each genre
    counts=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    total_ratings=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    for j in range(num_movies):
        movie_genre=movie_data[movie_data['movie_id']==j+1]
        
        rating=i_ratings[j][2]
        
        for p in range(18):
            x=movie_genre[genres[p]].as_matrix()[0]
            if(x==1):
                counts[p]=counts[p]+1
                total_ratings[p]=total_ratings[p]+rating
        avg_ratings=[]
        for a in range(18):
            if(counts[a]!=0):
                avg_ratings.append(total_ratings[a]/counts[a])
                 
            else:
                avg_ratings.append(0)
        line1=""        
        for p in avg_ratings:
            line1=line1+"\t"+str(p)
    f.write(line+line1+"\n") 
              
    print(i+1)
            
f.close       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        