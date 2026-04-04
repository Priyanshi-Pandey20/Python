class Vehicle:
    milege="10"
    color="blue"
    petrol="petrol"

#OBJECT CREATION
car = Vehicle()
print(car.color)
bike = Vehicle()
print(bike.milege)
aeroplane = Vehicle()
print(aeroplane.petrol)

class Car:
    brand="swift"

obj = Car()
print(obj.brand)

#INSTANCE ATTRIBUTE
class Student:
    college="ABC College"
    def __init__(self,name,course):#the object for which init is called in passed here (IT IS COMPULSORY TO PASS IT )
        print("Wheneve a new object is created I am called automatically")
        print(name)
        print(course)
student1 = Student("Sneha","Communication")#init method will be called
student2 = Student("Khushi","B.Tech")  

#METHODS

class Student:
    def __init__(self,name,listOfMarks):
        self.name = name
        self.listOfMarks = listOfMarks
    def average(self):
        sum = 0
        for eachval in self.listOfMarks:
            sum = sum+eachval
        average = sum/3
        print("Average is :",average)
student= Student("Avi",[99,90,98])
student.average()










