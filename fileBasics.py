file = open("mast.txt","r")
data = file.read()   #READING THE ENTIRE FILE 
dataFile = data.lower()

if "live" in dataFile:
    print("Yes Live word is present in file")

file = open("report.txt","w") #WRITING IN A FILE 
file.write("Hi I am learning Python")

file = open("report.txt","a") #APPENDING A FILE 
file.write("Hi I am learning Python")




