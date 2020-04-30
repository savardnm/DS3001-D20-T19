# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

tag_data = pd.read_csv('final-output.csv')
user_data = pd.read_csv('ratings-user-sorted.csv')
book_data = pd.read_csv('book_tags.csv')

all_users = list(set([row['user_id'] for index, row in user_data.iterrows()]))

output = pd.DataFrame(index = all_users, columns = [row['tag_id'] for index, row in tag_data.iterrows()])
counts = pd.DataFrame(index = all_users, columns = [row['tag_id'] for index, row in tag_data.iterrows()])

for user_index, user_row in user_data.iterrows():
    user_id = user_row['user_id']
    book_id = user_row['book_id']
    rating = user_row['rating']
    count = 0
    for book_index, book_row in book_data.iterrows():
        if (book_id == book_row['goodreads_book_id']):
            if (book_row['tag_id'] in output.columns):
                output[book_row['tag_id']][user_id] += rating
                counts[book_row['tag_id']][user_id] += 1.0
            count = count + 1
            if (count > 3):
                break

for index, row in output:
    for name, column in row:
        output[index][name] = output[index][name] / counts[index][name]
        

output.to_csv("absolute-final.csv", index=True)

print (output)
