import pandas as pd

df= pd.read_csv("movies.csv")
# print (df)

#  print first 7 row of the dataframe 
# print(df.head)

#  print last four row the dataframe
# print(df.tail(4))

# print random 5 row of the dataframe
# print(df.sample(5))
# dir(df.shape)

#  displaying industry is Bollywood
# print(df[df.industry=='Bollywood'])
#  displaying industry is Hollywood
# print(df[df.industry!='Hollywood'] )

#  displaying industry is Rajasthani 
# sdf= df[df.industry!='Hollywood']
# print(sdf)


print('All movies min = ',df.imdb_rating.min(),' Max=   ',df.imdb_rating.max(), ' Average= ',df.imdb_rating.mean())

df_h= df[df.industry!='Hollywood']
print('Bollywood movies min = ',df_h.imdb_rating.min(),' Max=   ',df_h.imdb_rating.max(), ' Average= ',df_h.imdb_rating.mean())

df_b= df[df.industry!='Bollywood']
print('Hollywood movies min = ',df_b.imdb_rating.min(),' Max=   ',df_b.imdb_rating.max(), ' Average= ',df_b.imdb_rating.mean())