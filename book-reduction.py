# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:27:55 2020

@author: Nathan
"""


import pandas as pd

book_data = pd.read_csv('book_tags.csv')
tag_data = pd.read_csv('final-output.csv')

book_output = pd.DataFrame(0.01, index = [], columns = ['goodreads_book_id', 'tag_id', 'count'])

count = 0
book_id = 0
total = 0
for index, row in book_data.iterrows():
    total += 1
    if(book_id != row['goodreads_book_id']):
        count = 0
        book_id = row['goodreads_book_id']
        #tag_count = float(row['count'])
    if((total%10000) == 0):
        print(total)
    if((row['tag_id'] in tag_data['tag_id'].values) and (count < 5)):
        #book_data['count'][index] = float(row['count'])/tag_count
        book_output = book_output.append(row, ignore_index = True)
        count += 1
    #if(total > 1000):
        #break



book_output.to_csv("shortened-books-2.csv", index=False)

print (book_output)