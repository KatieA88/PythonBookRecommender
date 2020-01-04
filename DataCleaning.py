#%%

#IMPORT LIBRARIES
import pandas as pd 

#%%

#IMPORT DATA
books = pd.read_csv('books.csv')
ratings = pd.read_csv('ratings.csv')
tags = pd.read_csv('tags.csv')
booktags = pd.read_csv('book_tags.csv')

#%%CLEAN DATA

#remove columns which will not be needed to generate book recommendations
books = books.drop(['best_book_id', 'work_id', 'isbn', 'isbn13', 'ratings_count', 'work_ratings_count', 'work_text_reviews_count', 'image_url', 'small_image_url', 'original_title', 'ratings_1', 'ratings_2', 'ratings_3', 'ratings_4', 'ratings_5', 'average_rating', 'books_count'], axis = 1)

#booktags = booktags.drop('count')

# Standardise language code for english to 'eng':
books['language_code'].replace({'en-US':'eng','en-GB':'eng','en-CA':'eng'}, inplace=True)


#%%
#clean up most used tags to create a more standardised list
tag_freq=booktags.groupby('tag_id').count().sort_values('count',ascending=False)['count']

popular_tags=tags[tags['tag_id'].isin(list(tag_freq.index[:200]))]

new_tag_ids = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,50]

new_tags = {1:'action', 2:'adult', 3:'biography', 4:'chick-lit', 5:'childrens', 6:'classics', 7:'comedy', 8:'coming-of-age', 9:'contemporary', 10:'crime', 11:'drama', 12:'family', 13:'fantasy', 14:'fiction',15:'friendship', 16:'historical', 17:'horror', 18:'romance', 19:'magic', 20: 'mystery', 21:'paranormal', 22:'sci-fi', 23:'philosphy', 24:'young-adult', 25:'thriller', 26:'war', 27:'women', 28:'adventure', 29: 'book_club', 30:'childhood', 31:'detective', 32: 'school', 33:'non-fiction', 34:'science', 50:'other'}

new_tag_map = {1540:1, 1542:1, 1642:2, 1659:2, 1691:28, 4605:3, 4949:29, 4985:29, 5051:29, 6750:4, 6828:30, 6857:5, 6888:5, 6960:5, 7404:6, 7457:6, 7725:7, 7852:8, 8055:9, 8067:9, 8076:9, 8517:10, 8527:10, 8533:10, 9336:31, 9886:11, 11221:12, 11305:13, 11370:13, 11376:13, 11743:14, 12600:15, 12680:7, 14370: 32, 14467:16, 14487:16, 14552:16, 14821:17, 15048:7, 15067:7,18318:14, 18326:14, 18367:14, 18640:18, 18886:19, 20288:14, 20926:20, 20939:20, 20957:20, 20989:20, 20989:20, 20994:20, 21689:33, 21773:33, 21989:14, 22034:14, 22973:21, 23471:23, 25438:14, 25630:18, 26138:18, 26735:32, 26771:22, 26785:22, 26816:34, 26837:22, 26842:22, 26894:22, 26897:22, 29011:21, 20976:25, 29083:25, 29852:24, 30358:25, 30386:25, 31617:13, 32130:26, 32686:27, 32989:24, 32996:24, 33009:26, 33012:26, 33114:26, 33124:26, 33165:26}

#%%
#add new tag id to booktags df
booktags['new_tag_id']=booktags['tag_id'].replace(new_tag_map)

#If tag is not in list then tag_id = 50 (other) 
booktags.loc[~booktags['new_tag_id'].isin(new_tags), 'new_tag_id']=50

#add new tag id to tags df
tags['new_tag_id']=tags['tag_id'].replace(new_tag_map)  

#create a column for tag ids. This will be replaced by dictionary values with the tag name.
booktags['new_tag_name']=booktags['new_tag_id']
booktags=booktags.replace({'new_tag_name': new_tags})

#remove duplication of tags across books including all "other" tags as all books are tagged with other
booktags = booktags.sort_values('goodreads_book_id', ascending=True).drop_duplicates(subset=['new_tag_id','goodreads_book_id'], keep='first')
booktags = booktags[booktags['new_tag_id'] != 50] 

#drop old tag id column
booktags = booktags.drop('tag_id', axis = 1)

#remane columns

booktags = booktags.rename(columns={'new_tag_id':'tag_id','new_tag_name': 'tag_name','goodreads_book_id':'book_id'})

tagcount = booktags.groupby('tag_name')['book_id'].count().sort_values(ascending=False)

#%%

#save csv files
books.to_csv(r'df_books.csv',index=False)
ratings.to_csv(r'df_ratings.csv',index=False)
booktags.to_csv(r'df_tags.csv',index=False)

