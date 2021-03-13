#importing a class 
import Class1 as Cls

Bob = Cls.Student

John = Cls.Student.from_dash("Preet-1002-9.0")
print(John.__dict__)
