class Student:
    def __init__(self,string):
        self.string = string

    @classmethod
    def get_string(cls,inp):
        cls.string= inp
        return cls

    @classmethod
    def print_string(cls):
        print(cls.string.upper())

s=Student
s.get_string("Bishesh")
s.print_string()