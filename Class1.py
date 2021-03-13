# Decorator and __name__ method in Python
class Student:
    def __init__(self, name, enroll, CGPI):
        self.name = name
        self.enroll = enroll
        self.CGPI = CGPI

    @classmethod
    def from_dash(cls,String):
        return cls(*String.split("-"))

Bob = Student("Bob", 1001 , 9.03)

if __name__ == "__main__":
    print(Bob.__dict__)
else:
    print("From Class1:-")
    print(Bob.__dict__)