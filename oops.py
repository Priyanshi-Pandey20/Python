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
    def __init__(self):
        print("Wheneve a new object is created I am called automatically")
student1 = Student()
student2 = Student()        




