import random 
import json

#giving range to guess the number from 1 to 100
number = random.randint(1,100)

#our initial guesses are zero
guesses = 0

print("       GUESSING A NUMBER GAME       ")
print("    GUESS A NUMBER FROM 1 TO 100    ")

while True :
    #asking user to input the guess he wants to take
    guess = int(input("Take a guess : "))
    #incrementing the number of guesses user makes to showcase the number of guesses to guess the corrct number 
    guesses += 1

#Giving conditions for the game for high and low guesses 
    if (number > guess):
        print("you guessed low ,please guess a bit higher") 
    elif (number < guess ):
        print("you guessed high ,please guess a bit lower")
    else:
        print(f"🎊congratulations 🎉 you guessed it right in {guesses} attempts🎊")
        #to break out of loop after guessing the correct number 
        break



#My json file name in variable
file_name = "leaderboard01.json"

#try to read this file if the file exits proceed if not then stop execution and go to except  block of code
try :
    with open(file_name,"r") as f :
        leaderboard = json.load(f)

#if the file does not exist create a temporary empty list 
except :
    leaderboard = []

#after game ends take name and set attempts to number of guesses the user took
name = input("enter your name : ")
attempts = guesses

#append that info in the list 
leaderboard.append({
    "name" : name ,
    "attempts" : attempts
})

#sort out the ranking based on less number of attempts
leaderboard.sort(key=lambda x : x["attempts"])

#store only till range 3 i.e only top 3 players info
leaderboard =leaderboard[:3]

#take the data from list and write it in the file and indent 4 space every time 
with open(file_name ,"w") as f :
    json.dump(leaderboard,f ,indent = 4)