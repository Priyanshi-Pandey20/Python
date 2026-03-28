student = {
    "name":"Aditya",
    "city":"Jabalpur",
    "age":"21",
    "rollNumber":60
}
print(type(student))
print(student["name"])
student["favSubject"] = "Maths"
print(student)
student.pop("age")
print(student)