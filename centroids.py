# -*- coding: utf-8 -*-
"""
Created on Sat May  9 22:06:58 2020

@author: Nathan
"""


import pandas as pd

user_data = pd.read_csv('final-csv/clustered_data.csv')

centroids = pd.DataFrame(3.0,index=[str(i) for i in range(17)],columns=user_data.columns)
print([str(i) for i in range(17)])
centroids['user_count']=1
print(centroids)

for index,row in user_data.iterrows():
    cluster = str(int(row['cluster']))
    centroids.loc[cluster,'user_count']+=1
    if(index%100 == 0):
        print(index)
    centroids.loc[cluster,'cluster']=cluster
    for tag_id in row.iteritems():
        if(tag_id[0] != 'cluster' and tag_id[0] != 'user_count'):
            if(row[tag_id[0]] == 3.0):
                centroids.loc[cluster, tag_id[0]]+=centroids.loc[cluster, tag_id[0]]/centroids.loc[cluster, 'user_count']
            else:
                centroids.loc[cluster, tag_id[0]]+=row[tag_id[0]]

print(centroids['user_count'])
for column in centroids.iteritems():
    if(column[0] != 'user_count' and column[0] != 'cluster'):
        centroids[column[0]] = centroids[column[0]]/centroids['user_count']
    
print(centroids)

centroids.to_csv("centroids.csv", index=True)