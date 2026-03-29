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

marks={}
marks["Maths"] = 98
marks["Science"] = 92
marks["Geography"] =90
print(marks)

meanings = {
    "hola":"Hello",
    "persuasive":"collision of two bodies",
"possessive":"protective"
}
print(meanings)

frnd1 = {"priyanshi","priya","palak"}
frnd2 = {"kajal","poornima"}
friends = frnd1.union(frnd2)
friends = frnd1.intersection(frnd2)
print(friends) 
