import pandas as pd
no_of_movies=9740
data=pd.read_csv('./ml-latest-small/movies.csv',usecols=[0,1])
movies={}
length=data.shape[0]
max_movieID=data.iloc[length-1,0]
for i in range(0,length):
    row=data.iloc[i,[0,1]]
    movies[row[0]]=row[1]

ratings={}
rating_length=100800
data=pd.read_csv('./ml-latest-small/ratings.csv',usecols=[0,1,2])
len2=data.shape[0]
max_userID=data.iloc[len2-1,0]
ratings={}
for i in range(0,len2):
    row=data.iloc[i,[0,1,2]]
    try:
        if(row[1]<=max_movieID):
            ratings[int(row[0])][row[1]]=row[2]
    except KeyError:
        ratings[int(row[0])]={}
# print(ratings)
