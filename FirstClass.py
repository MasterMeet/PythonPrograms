# How to create a class in Python
class Student:
    def __init__(self, name, enroll, CPI):
        self.name = name
        self.enroll = enroll
        self.CPI = CPI


Meet = Student("Meet", 186200316007, 9.03)
print(Meet.__dict__)
