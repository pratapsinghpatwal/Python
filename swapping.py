# Python program to swap two variables

x = 5
y = 10

# To take inputs from the user
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: ',x)
print('The value of y after swapping: ',y)
