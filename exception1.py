x=input("Enter the value number 1  ")
y=input("Enter the value number 1  ")

try :
  z=int(x)/int(y)

except Exception as e :
  print ("Exception is  ",e)
  z=0
print("The divison of  a and b is  ",z)
