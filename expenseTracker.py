expensesList = [] #list of expenses

print("WELCOME TO EXPENSE TRACKER : ")

while True:
    print("======MENU=======")
    print("1. Add Expense")
    print("2.View All Expenses")
    print("3.View Total Karcha ")
    print("4.Exit")

    choice = int(input("Please enter your choice:"))

    if(choice == 1):
        date = input("Enter the date : ")
        category = input("Enter the category: ")
        description= input("Enter the detail: ")
        amount = float(input("Enter the amount: "))

        expenses={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expensesList.append(expenses)
        print("Expenses added successfully!!!")

#VIEW ALL EXPENSES

    if(choice == 2):
        if(len(expensesList) == 0):
            print("No Expenses Added: ")
        else:
            print("===THIS IS ALL YOUR EXPENSES===") 
            count = 1
            for eachKarcha in expensesList:
                print(f" Expense Number {count} -> {eachKarcha["date"]}, {eachKarcha["category"]},{eachKarcha["description"]},{eachKarcha["amount"]} ")
                count = count + 1

#View Total Spending
    if(choice == 3):
        total = 0
        for eachKarcha in expensesList:
            total = total + eachKarcha["amount"]
            
        print("Total Spended Money : ", total)    


#View Total Spending
    elif(choice == 4):
        print("THANK YOU!!!!")   
        break
    else:
        print("Invalid Choice")                         









      
    


