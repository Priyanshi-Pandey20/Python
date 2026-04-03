import os

file = open("mast.txt","r")
data = file.read()   #READING THE ENTIRE FILE 
dataFile = data.lower()

if "live" in dataFile: #CHECK LIVE KEYWORD EXISTS IN A FILE OR NOT
    print("Yes Live word is present in file")

file = open("report.txt","w") #WRITING IN A FILE 
file.write("Hi I am learning Python")

file = open("report.txt","a") #APPENDING A FILE 
file.write("Hi I am learning Python")
file.close()

# with open("mast.txt","r") as f:  #WITH KEYWORD 
#     data = f.read()
#     print("file data",data)

# with open("mast.txt","r") as f: #READING THE FILE LINE BY LINE
#     line1 = f.readline()   
#     line2 = f.readline()   
#     line3 = f.readline() 
#     data= f.read()
#     print("line1",line1)
#     print("line2",line2)
#     print("line3",line3)  
#     print("file data",data)

# with open("mast.txt","r") as f: #READING ALL THE LINES IN ONE GO 
#     line = f.readlines()
#     print(line)

with open("mast.txt","r") as f: #TOTAL NO. OF LINES 
    line = f.readlines()
    print(len(line))

os.rename("report.txt","hello.txt")    










