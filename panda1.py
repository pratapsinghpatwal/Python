import csv

def calculaterating(data,industry=None):
  rating=[]
  for row in data :
    if row[3]!='NULL' and (not industry or row[1]==industry) :
      rating.append(float(row[3]))
  maxrating=max(rating)
  minrating=min(rating)
  avgrating=sum(rating)/len(rating)
  return maxrating,minrating,avgrating

with open ("movies.csv") as f :
  data=list(csv.reader(f))
  header=data[0]
  # print(header)
  data=data[1:]
  # print(header)

maxrat,minrat,avgrat=calculaterating(data)
print(f'All records : min rating ={minrat}  max rating {maxrat} average rating {avgrat}')

maxrat,minrat,avgrat=calculaterating(data,industry='Bollywood')

print(f'Bollywood Record : min rating ={minrat}  max rating {maxrat} average rating {avgrat}')

maxrat,minrat,avgrat=calculaterating(data,industry='Hollywood')

print(f'Hollywood Record : min rating ={minrat}  max rating {maxrat} average rating {avgrat}')