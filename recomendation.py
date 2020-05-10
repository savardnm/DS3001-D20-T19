# -*- coding: utf-8 -*-
"""
Created on Fri May  8 21:10:58 2020

@author: Nathan
"""
import pandas as pd
import numpy as np
import math  


user_data = pd.read_csv('final-csv/clustered_data.csv')
rating_data = pd.read_csv('raw-data/ratings.csv')
book_data = pd.read_csv('raw-data/books.csv')
centroids = pd.read_csv('final-csv/centroids.csv')
ratings = []
alpha = 0.8



def get_recommendations(cluster):
    user_data = pd.read_csv('final-csv/clustered_data.csv')
    rating_data = pd.read_csv('raw-data/ratings.csv')
    book_data = pd.read_csv('raw-data/books.csv')
    ratings = []
    print('getting recommendations for cluster: ', cluster)
    book_data = pd.read_csv('raw-data/books.csv')
    book_data['recommendation']=0.0
    book_data['count']=0.0
    cluster_data=user_data.loc[user_data['cluster']==cluster]
    users=cluster_data['user_id']
    total_users = len(cluster_data.index)
    for user in users.iteritems():
        user_ratings=rating_data.loc[rating_data['user_id']==user[1]]
        #print(user_ratings)
        for index,row in user_ratings.iterrows():
            rating=row['rating']
            i_row = np.where(book_data['id']== row['book_id'])[0][0]
            book_data.at[i_row,'recommendation']+=rating
            book_data.at[i_row,'count']+=1
            pass
        pass
    for index,row in book_data.iterrows():
        if(row['count']!=0):
            tup=(row['id'], (row['recommendation']/row['count'])*alpha + (5*row['count']/total_users)*(1-alpha))
            ratings.append(tup)
            pass
        pass
    
    ratings.sort(key=lambda x:x[1], reverse = True)
    
    return ratings



def get_cluster(user_input):
    min_dist = 0
    for index,row in centroids.iterrows():
        row.rename(index=str)
        errors = []
        for tup in user_input:
            if(row.get(str(tup[0])) != 3 and tup[1]!= 3):
               errors.append( (row.get(str(tup[0]))-tup[1])**2 )
               print("here")
        dist=math.sqrt(sum(errors))
        if (dist > min_dist):
            min_dist = dist
            cluster=row['cluster']
            print('new cluster', cluster)
            pass
        pass
    return cluster
            
            
        
    pass           
    
#get_recommendations(8)
#print(book_data)
#print(ratings[0:30])
    
