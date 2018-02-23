class Student:
    def __init__(self,fname,lname):
        self.fname= fname
        self.lname= lname
        self.email= self.fname+'.'+self.lname+'@'+'deerwalk.edu.np'

    def get_email(self):
        return self.email.lower()



std= Student('Bishesh','Katwal')
print(std.get_email())