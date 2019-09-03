class student:
    def __init__(self):
        self.stud_id = None
        self.marks = None
        self.age = None

    def validate_marks(self):
        if self.marks in range(0,101):
            return True
        return False

    def check_qualification(self):
        if self.validate_marks():
            if self.marks>=65:
                return True
        return False

    def validate_age(self):
        if self.age>20:
            return True
        return False

    def set_attributes(self,s,m,a):
        self.stud_id = s
        self.marks = m
        self.age = a

    def get_attributes(self):
        print("Student id:",self.stud_id)
        print("Marks:",self.marks)
        print("Age:",self.age)

n = int(input())
s = []
for i in range(n):
    
s1 = student()
s1.set_attributes("1bm17cs074",78,21)
s2 = student()
s2.set_attributes("1bm17cs075",62,19)
print(s1.validate_marks())
print(s1.validate_age())
print(s2.validate_marks())
print(s2.validate_age())
s1.get_attributes()
s2.get_attributes()
if(s1.check_qualification()):
    print("Student1 eligile")

if(s2.check_qualification()):
    print("Student2 eligile")
    





        
