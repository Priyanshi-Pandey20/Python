#Rule Based AI Chatbot


import datetime
import time

name = input("Swagat hai! enter your name: ")
presentHour = datetime.datetime.now().hour


if 5<= presentHour <=11:
    print("GOOD MORNING!!☀️",name)
elif 11 <=presentHour <= 17:
    print("GOOD AFTERNOON!!🌤️",name)
elif 17 <= presentHour <= 20:
    print("GOOD EVENING!!🌇",name)  
else:
    print("GOOD NIGHT!!🌙",name)          


print("Namaste! Welcome to Your ChatBot")
print("You can ask me basic question, Type 'bye' to exit from the bot")

#Chatbot Memory Creation!

responses = {
    "hello":"Hi,welcome. How can I help you?",
    "how are you":"I am very fine. Thank you",
    "who are you":"I am smart AI chatbot",
    "motivate me":"Keep going. Every bug of your project makes you a better developer",
    "happy":"Great to hear that",
    "what are function":"Go to Chapter 7 of python course ",
}

#Method to get response of ChatBot

def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I dont't Know that!😢 I will learn that soon!🙂"    


#Take user input
while True:
    userInput = input("Please ask your question:")
    reply = getResponseOfBot(userInput)
    print("Bot Response :",reply)

    if "bye" in userInput.lower():
        break

   
