# Python program to find H.C.F of two numbers

x =int(input("Enter the first values"))
y=int(input("Enter the  Second values"))

# choose the smaller number
if x > y:
        smaller = y
else:
  smaller = x
for i in range(1, smaller+1):
      if((x % i == 0) and (y % i == 0)):
           hcf = i 
    
print("The H.C.F. is", hcf)
