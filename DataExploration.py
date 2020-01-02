#%%

#IMPORT LIBRARIES
import pandas as pd 
import matplotlib.pyplot as plt

#%%

#IMPORT DATA
books = pd.read_csv('books.csv')
ratings = pd.read_csv('ratings.csv')
tags = pd.read_csv('tags.csv')
booktags = pd.read_csv('book_tags.csv')
#%%

#EXPLORATORY DATA ANALYSIS- RATINGS
#%%

#first we'll look to understand the quality of the usder and ratings data
reader_ratings=ratings.groupby('user_id')['rating'].count().sort_values()
print(reader_ratings.describe())
plt.figure()
plt.hist(reader_ratings);
plt.xlabel('Num Books Rated')
plt.ylabel('Num Users')
plt.title('Numb Books Rated Per Reader')
plt.show()

#minumum number of ratings per user is 19 with a mean of 111 across 53k users
#%%

#then we want to understand the distribution of books across the different ratings?
print (ratings.agg(['count','nunique']))
plt.figure()
plt.hist(ratings['rating'], bins=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5],rwidth=0.8, color = 'darkblue');
plt.xlabel('Ratings')
plt.ylabel('Counts')
plt.title('Book Ratings')
plt.show()
#the graph shows that the majority of books are rated 4 and 5

#%%

#now we'll look to understand the amount of ratings per book
book_ratings = ratings.groupby('book_id')['rating'].count().sort_values(ascending=False)
x=list(book_ratings.sort_index().index)
y=list(book_ratings.sort_index())

plt.figure()
plt.scatter(x,y,s=0.5,alpha=0.2)
plt.title('Number of Ratings and book_id')
plt.xlabel('book_id')
plt.ylabel('Number of Ratings')
plt.yscale('log')
plt.show()

#books with lower (earlier) book ids show more ratings. This could indicate that the book has been available for rating for longer if it has an earlier id. Will need to ensure that the recommendation engine is not bias towards earlier books because they have more ratings.

#%%

#what are the most rated books?
most_rated = book_ratings.index[:20]
print (most_rated)

#%%

#EXPLORATORY DATA ANALYSIS- BOOKS
#%%

book_count = books['books_count']
plt.figure()
plt.hist(book_count);
plt.xlabel('x')
plt.ylabel('y')
plt.title('Book Count by Book ID')
plt.show()

#%%
author_count = books.groupby('authors')['book_id'].count().sort_values(ascending=False)
most_featured_authors = author_count.index[:20]
print(most_featured_authors)

#the most featured authors are prominent names such as Stephen King, Terry Pratchet etc

#%%
print(books['language_code'].describe())

#there are 25 languages featured, of which English is most popular. There are several version of English (e.g. Eng, Eng-US, which will need to be cleaned.)

lang_count = pd.DataFrame(books.groupby('language_code')['book_id'].count().sort_values(ascending = True)).reset_index()
plt.figure()
lang = lang_count['language_code']
count = lang_count['book_id']
plt.barh(lang, count)
plt.xlabel('Num Books')
plt.ylabel('Language')
plt.title('Book Count by Language')
plt.show()

#%%

#what were the titles of the most rated books from the earlier analysis
books[books['book_id'].isin(most_rated)]['title']

#%%

#EXPLORATORY DATA ANALYSIS- TAGS
#%%
#how many different tags are there?
print(booktags['tag_id'].nunique())

#which tags are most used?
tag_freq=booktags.groupby('tag_id').count().sort_values('count',ascending=False)['count']
print(tags[tags['tag_id'].isin(list(tag_freq.index[:20]))])
