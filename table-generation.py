# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

tag_data = pd.read_csv('final-output.csv')
user_data = pd.read_csv('ratings-2.csv')
book_data = pd.read_csv('shortened-books.csv')
id_data = pd.read_csv('books.csv')

print(id_data.iloc[1-1]['book_id'])
all_users = list(set([row['user_id'] for index, row in user_data.iterrows()]))

output = pd.DataFrame(0.1,index = all_users, columns = [row['tag_id'] for index, row in tag_data.iterrows()])
counts = pd.DataFrame(0,index = all_users, columns = [row['tag_id'] for index, row in tag_data.iterrows()])
total = 0
for user_index, user_row in user_data.iterrows():
    user_id = user_row['user_id']
    book_id = id_data.iloc[user_row['book_id']-1]['book_id']
    rating = user_row['rating']
    count = 0
    if((total%1000)==0):
        print(total)
    total += 1
    done = False
    
    search = book_data.loc[lambda book_data: book_data['goodreads_book_id'] == book_id]
    
    for book_index, book_row in search.iterrows():
        if (book_row['tag_id'] in output.columns):
            output[book_row['tag_id']][user_id] += rating
            counts[book_row['tag_id']][user_id] += 1.0
    
print(output)
    

for index, row in output.iterrows():
    for name, column in row.iteritems():
        if(output[name][index]==0.1):
            output[name][index] = 3.0
        else:
            output[name][index] = (output[name][index]-0.1) / max(counts[name][index],1)

print (output)
output.to_csv("absolute-final-2.csv", index=True)
