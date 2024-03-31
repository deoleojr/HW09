#!/usr/bin/env python
# coding: utf-8

# In[5]:


##TASK 01
import os
os.getcwd()
directory_path=r'C:\Users\deole\OneDrive\Desktop\DS\DS5100\HW 8'
os.chdir(directory_path)


import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        if book_list is None:
            self.book_list = pd.DataFrame({'book_name': [], 'book_rating': []})
        else:
            self.book_list = book_list

    def add_book(self, book_name, rating):
        if not self.has_read(book_name):
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print(f"{self.name} has already read {book_name}.")

    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]

if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    print("Initial number of books read:", test_object.num_books_read())
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("The Martian", 5)
    test_object.add_book("War of the Worlds", 3)  # Trying to add a book that already exists
    print("Number of books read after adding:", test_object.num_books_read())
    print("Favorite books:")
    print(test_object.fav_books())


# In[ ]:




