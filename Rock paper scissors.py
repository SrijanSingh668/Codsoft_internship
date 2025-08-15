#Rock Paper and scissors
import random

#making  a list to select random moves
words = ["rock", "paper", "scissors"]

print("=========== ROCK PAPER SCISSORS ========== ")
print()
while True:
    
    #for taking random choice by the computer
    random_word = random.choice(words)
    
    print("Press 1 for Rock ✊" )
    print("Press 2 for Paper 🖐" )
    print("Press 3 for Scissors ✌️" )
    choice=input("Enter your move ✊,🖐,✌ (1/2/3):")
    
    #conditions for wining and tie
    if (choice=="1" and random_word =="scissors") or (choice=="2" and random_word=="rock") or (choice=="3"and random_word=="paper"):
        print("Congratulations!🎉 You Win The Game")
    elif(choice=="2" and random_word =="scissors") or (choice=="3" and random_word=="rock") or (choice=="1"and random_word=="paper"):
        print("The computer wins the game")
    elif(choice=="3" and random_word =="scissors") or (choice=="1" and random_word=="rock") or (choice=="2"and random_word=="paper"):
        print("There is a Tie")
    else:
        print("This is a Invalid Choice")
    print("The game over")

    #to continue the game
    ch=input("Do you want to play again? {yes/no or y/n or Yes/No} ")
    if ch not in ["yes","y","Yes"]:
        break


