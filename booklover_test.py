#!/usr/bin/env python
# coding: utf-8

# In[10]:


##TASK02
import os
os.getcwd()
directory_path=r'C:\Users\deole\OneDrive\Desktop\DS\DS5100\HW 8'
os.chdir(directory_path)

import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        test_object = BookLover("John Doe", "johndoe@example.com", "fiction")
        test_object.add_book("Book 1", 4)
        self.assertTrue(test_object.has_read("Book 1"))

    def test_2_add_book(self):
        test_object = BookLover("Jane Smith", "janesmith@example.com", "mystery")
        test_object.add_book("Book 2", 3)
        test_object.add_book("Book 2", 5)
        self.assertEqual(test_object.num_books_read(), 1)

    def test_3_has_read(self):
        test_object = BookLover("Alice Johnson", "alice@example.com", "fantasy")
        test_object.add_book("Book 3", 5)
        self.assertTrue(test_object.has_read("Book 3"))

    def test_4_has_read(self):
        test_object = BookLover("Bob Brown", "bob@example.com", "nonfiction")
        test_object.add_book("Book 4", 4)
        self.assertFalse(test_object.has_read("Book 5"))

    def test_5_num_books_read(self):
        test_object = BookLover("Eva Williams", "eva@example.com", "romance")
        test_object.add_book("Book 5", 2)
        test_object.add_book("Book 6", 3)
        self.assertEqual(test_object.num_books_read(), 2)

    def test_6_fav_books(self):
        test_object = BookLover("Michael Davis", "michael@example.com", "thriller")
        test_object.add_book("Book 7", 5)
        test_object.add_book("Book 8", 4)
        test_object.add_book("Book 9", 3)
        fav_books = test_object.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))

if __name__ == '__main__':
    unittest.main(verbosity=3)

!ls - lR
!pip install -e .



