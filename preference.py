#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 08:10:43 2018

@author: pallavi
"""
import pandas as pd
import numpy as np

#find preference

header = ['user_id' ,'Action' , 'Adventure' , 'Animation' ,
              'Children', 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,
              'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,
              'Thriller' , 'War' , 'Western']

avgRating = pd.read_csv('data/normalized_avg_ratings.txt', sep='\t', names=header)
avgRating=avgRating.drop(['user_id'],axis=1)
avgRating=np.array(avgRating.as_matrix())

consumptionRatio = pd.read_csv('data/consumptionRatio.txt', sep='\t', names=header)
consumptionRatio=consumptionRatio.drop(['user_id'],axis=1)
consumptionRatio=np.array(consumptionRatio.as_matrix())

preference=avgRating*consumptionRatio

np.savetxt('data/preference.txt', preference, delimiter='\t',newline='\n')
 
