# -*- coding: utf-8 -*-
"""
Created on Fri May  8 21:10:58 2020

@author: Nathan
"""
import pandas as pd
import numpy as np


user_data = pd.read_csv('final-csv/absolute-final.csv')
rating_data = pd.read_csv('raw-data/ratings.csv')
book_data = pd.read_csv('raw-data/books.csv')
ratings = []
alpha = 0.8


def get_recommendations(cluster):
    book_data['recommendation']=0.0
    book_data['count']=0.0
    cluster_data=user_data.loc[user_data['cluster']==cluster]
    #print(cluster_data)
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
    bah = 0
    for index,row in book_data.iterrows():
        if (bah < 10):
            print(row['count'])
            bah +=1
        if(row['count']!=0):
            tup=(row['id'], (row['recommendation']/row['count'])*alpha + ((row['recommendation']/row['count'])*row['count']/total_users)*(1-alpha))
            ratings.append(tup)
            pass
        pass
    
    ratings.sort(key=lambda x:x[1], reverse = True)
    
    #return ratings *alpha + (5*row['count']/total_users)*(1-alpha)
            
    
get_recommendations(6)
print(book_data)
print(ratings[0:30])
    
