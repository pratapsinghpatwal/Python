class student :
    def check_pass_fail(self) :
        if self.marks >= 40 :
            return True
        else :
            return False

student1 =student()
student1.name="Raju"
student1.marks=72

did_pass= student1.check_pass_fail()
print(did_pass)

student2 =student()
student2.name="Rani"
student2.marks=1

did_pass= student2.check_pass_fail()
print(did_pass)
