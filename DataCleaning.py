#%%

#IMPORT LIBRARIES
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

#%%

#IMPORT DATA
books = pd.read_csv('books.csv')
ratings = pd.read_csv('ratings.csv')
tags = pd.read_csv('tags.csv')
booktags = pd.read_csv('book_tags.csv')