import random 

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

name = str(input("Enter player name : "))
score = guesses

with open("scores01.txt","a") as f:
    f.write(f"player : {name} , {score} \n")