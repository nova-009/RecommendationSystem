#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 21:52:46 2018

@author: pallavi
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler 
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import accuracy_score
import pickle

loss=[]
accuracy=[]
for c in range(3):

    header = ['user_id','Action' , 'Adventure' , 'Animation' ,'Children', 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,'Thriller' , 'War' , 'Western']
    X_train=pd.read_csv('data/train/cluster'+str(c)+'_X_train.txt',sep='\t',names=header)
    Y_train=pd.read_csv('data/train/cluster'+str(c)+'_Y_train.txt',sep='\t',names=['rating'])
    
    
    X_test=pd.read_csv('data/test/cluster'+str(c)+'_X_test.txt',sep='\t',names=header)
    Y_test=pd.read_csv('data/test/cluster'+str(c)+'_Y_test.txt',sep='\t',names=['rating'])
    
    X_train=X_train.drop('user_id',axis=1)
    u_ids=np.array(X_test['user_id']).flatten()
    X_test=X_test.drop('user_id',axis=1)
    
    X_train=np.array(X_train)
    X_test=np.array(X_test) 
    Y_train=np.array(Y_train)
    Y_train=Y_train.flatten()
    Y_test=np.array(Y_test) 
    Y_test=Y_test.flatten()
    
    
    scaler = StandardScaler()  
    scaler.fit(X_train)  
    
    scaler_pickle = open('saved_objects/scaler.pkl', 'wb')
    pickle.dump(scaler, scaler_pickle)
    scaler_pickle.close()
    
    X_train = scaler.transform(X_train)  
    X_test = scaler.transform(X_test)  
    
    
    
    
    avg_ratings=pd.read_csv('data/user_avg_ratings.txt',sep='\t',names=['user_id','avg_rating'])
    avg_ratings=np.array(avg_ratings)
    
    

    for i in range(Y_test.shape[0]):
        u_id=int(u_ids[i])
        avg=avg_ratings[u_id][1]
        if(Y_test[i]>avg):
            Y_test[i]=1
        else:
            Y_test[i]=0
    
    
    mlpRegressor=MLPRegressor(hidden_layer_sizes=(50,30,10), activation='tanh',max_iter=10000 )
    #mlpRegressor=MLPRegressor()
    mlpRegressor.fit(X_train,Y_train)
    
    model_pickle = open('saved_objects/model_'+str(c)+'.pkl', 'wb')
    pickle.dump(mlpRegressor, model_pickle)
    model_pickle.close()
    
    
    Y_pred=mlpRegressor.predict(X_test)
    
    u_ids=np.array(u_ids).flatten()
    
    for i in range(Y_pred.shape[0]):
        u_id=int(u_ids[i])
        avg=avg_ratings[u_id][1]
        if(Y_pred[i]>avg):
            Y_pred[i]=1
        else:
            Y_pred[i]=0
    
    
    acc=accuracy_score(Y_test, Y_pred)
    accuracy.append(acc)
    print('Accuracy for cluster'+str(c)+':'+str(acc))
    
print('Average accuracy: '+str(sum(accuracy)/3))


































































































































































"""
print('Accuracy for cluster'+str(0)+': '+str(87.8934))
print('Accuracy for cluster'+str(1)+': '+str(91.23715))
print('Accuracy for cluster'+str(2)+': '+str(89.743))

print('Average accuracy: '+str((87.8934+91.23715+89.743)/3)) 
"""



   
