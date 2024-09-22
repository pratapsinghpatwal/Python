# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

print(" \n  Second 3 X 3  \n")

for r in range(3):
   # iterate through columns of Y
   for c in range(3):
        print (X[r][c] , end =" ")
   print()

print(" \n  Second 3 X 4  \n")
for r in range(3):
   # iterate through columns of Y
   for c in range(4):
        print (Y[r][c] , end =" ")
   print()

