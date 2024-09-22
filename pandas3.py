import pandas as pd

df=pd.read_csv('movies.csv')

#  display rows and column in the datafram
print(df.shape)

#  display all the columns

print(df.columns)

#  display unique data of the datafram

dfu=df.industry.unique()
print(dfu)

#  display all the unique 

dff=df['language'].unique()
print(dff)

dfc=df.industry.value_counts()
print(dfc)

dfl=df['language'].value_counts()
print(dfl)
