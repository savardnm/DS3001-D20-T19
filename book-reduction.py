# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:27:55 2020

@author: Nathan
"""


import pandas as pd

book_data = pd.read_csv('book_tags.csv')

book_output = pd.DataFrame(index = [], columns = ['goodreads_book_id', 'tag_id', 'count'])

count = 0
book_id = 0
total = 0
for index, row in book_data.iterrows():
    count += 1
    total += 1
    if((total%1000) == 0):
        print(total)
    if(count < 3 ):
        book_output = book_output.append(row, ignore_index = True)
    if(book_id != row['goodreads_book_id']):
        count = -1
        book_id = row['goodreads_book_id']



book_output.to_csv("shortened-books.csv", index=False)

print (book_output)