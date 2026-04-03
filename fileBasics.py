file = open("mast.txt","r")
data = file.read()
dataFile = data.lower()

if "live" in dataFile:
    print("Yes Live word is present in file")

file = open("report.txt","a")
file.write("Hi I am learning Python")


