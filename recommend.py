import pandas as pd
import numpy as np
import math
import operator
from parse import no_of_movies,movies,ratings,len2,length,max_movieID,max_userID
################################
my_rating={}
# for i in movies.keys():
#     my_rating[i]=5*round(np.random.rand(),5)
# my_rating[5772]=0
# print(my_rating)
my_rating[858]=5.0
my_rating[318]=5.0

# my_rating[318]=0.0
# my_rating[2959]=2.50
# my_rating[102]=4.87
# my_rating[500]=1.24
# my_rating[700]=3.43
# my_rating[999]=3.43
my_keys=my_rating.keys()

################################
ratings
similarity=[0 for x in range(1,max_userID+2)]
print('1.Pearson criterion')
print('2.Euclid Criterion')


def get_pearson_similarity(arr,value,my_rating):
    n=len(arr)
    if n==0:
        return 0
    sum1=sum2=sum1sq=sum2sq=sump=0
    for x in arr:
        sum1+=value[x]
        sum1sq+=pow(value[x],2)
        sum2+=my_rating[x]
        sum2sq+=pow(my_rating[x],2)
        sump+=value[x]*my_rating[x]
    num=sump-(sum1*sum2)/n
    den=math.sqrt((sum1sq-pow(sum1,2)/n)*(sum2sq-pow(sum1,2)/n))
    if(den==0):
        return 0
    else:
        return num/den
    

def pearson_score(similarity,ratings,my_keys,my_rating):
    for key,value in ratings.items():
        arr=[x for x in value.keys() if x in my_keys]
        similarity[key]=get_pearson_similarity(arr,value,my_rating)
    



def euclid_score(similarity,ratings,my_keys,my_rating):
    for key,value in ratings.items():
        sum=0
        for movie,rating in value.items():
            if movie in my_keys:
                sum+=(my_rating[movie]-rating)**2
        sum=math.sqrt(sum)
        similarity[key]=round(1/(1+sum),5)

ch=input('Enter your choice:')
if ch==1:
    pearson_score(similarity,ratings,my_keys,my_rating)
else:
    euclid_score(similarity,ratings,my_keys,my_rating)

score={}
threshold_user=100
for movieId in movies.keys():
    sim_score=0
    sim_sum=0
    count_1=0
    for key,value in ratings.items():
        if movieId in value.keys():
            count_1+=1
            sim_score+=similarity[key]*value[movieId]
            sim_sum+=similarity[key]
    if sim_sum!=0 and count_1>=threshold_user:
        score[movieId]=round(sim_score/sim_sum,5)
        if score[movieId]>=4.9 and score[movieId]<=5.1:
            print('*************',sim_score,sim_sum,'******************8')
    else:
        score[movieId]=0
sorted_score=dict(sorted(score.items(), key=operator.itemgetter(1),reverse=True))
movies_display=10
count=1
for key,value in sorted_score.items():
    if key not in my_keys:
        print("{}:: {}".format(movies[key],value))
        count+=1
        if count>movies_display:
            break
# print(sorted_score[318])
