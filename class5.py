class student :
    def check_pass_fail(self) :
        if self.marks >=40 :
            return True
        else :
            return False
# initializing the class member variable or class constructor

    def  __init__ (self,name,marks) :
        self.name=name
        self.marks=marks

student1=student("Raju",43)   # creating an object of the class
student2=student("Ravi",3)     # creating an object of the class

did_pass=student1.check_pass_fail()
print(did_pass)

did_pass=student2.check_pass_fail()
print(did_pass)
