# Program to add two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for r in range(len(X)):
 
   # iterate through columns
   for c in range(len(X)):
        result[r][c] = X[r][c] + Y[r][c]

for r in result:
   print(r)
