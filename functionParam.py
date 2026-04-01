
def average(a,b):
    averageValue = (a+b)/2
    print(averageValue)

average(5,10)
average(7,10)

def show_age(name,age):
    print(f"{name} is {age} years old")
show_age("Priyanshi",25)    


def sum(a,b):
    addno = a+b
    diffno = a-b
    print(addno)
    print(diffno)

sum(5,5)
sum(10,5)

def multiply(a,b):
    return(a*b)

result = multiply(9,9)
print(result)

def countvowelsandconsonent(userInput):
    vowels = "aeiouAEIOU"
    countVowel = 0
    countConsonent = 0

    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
                countVowel+=1
            else:
                countConsonent+=1
    return countVowel,countConsonent

vowels,consonent = countvowelsandconsonent("Priyanshi Pandey")     
print(vowels,consonent)           



