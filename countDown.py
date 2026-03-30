import time
count = int(input("Enter the counter num: "))

print("Countdown starts now...")
for i in range(count,0,-1):
    print(i)
    time.sleep(1)
print("HAPPY BIRTHDAY!!!")    

