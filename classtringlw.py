class Triangle:
    def __init__(self,a,b,c):
        self.side1=a
        self.side2=b
        self.side3=c
    
    def Perimeter(self):
        p=self.side1+self.side2+self.side3
        return p

T1=Triangle(3,4,5)      
print(T1.Perimeter())
