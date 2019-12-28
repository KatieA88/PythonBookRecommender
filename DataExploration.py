#import libraries
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


#import data
books = pd.read_csv('books.csv')
ratings = pd.read_csv('ratings.csv')

#exploratory data analysis

print (ratings.agg(['count','nunique']))

plt.hist(ratings['rating'], bins=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5],rwidth=0.8, color = 'darkblue');
plt.xlabel('Ratings')
plt.ylabel('Counts')
plt.title('Book Ratings')
plt.show()

numreaderratings=ratings.groupby('user_id')['rating'].count().sort_values()
print(numreaderratings.describe())

plt.hist(numreaderratings, color = 'darkblue');
plt.xlabel('Number of Books Rated')
plt.ylabel('Number of Users')
plt.title('Number of Books Rated by each Reader')
plt.show()