import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: Rock, Paper, or Scissors")

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    #Get user's choice
    user_choice = input("Your choice: ").capitalize()

    if user_choice not in choices:
        print("Invalid choice. Please choose Rock, Paper or Scissors.")
        return
    
    print(f"The computer choose: {computer_choice}")

    #Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"): 
        print("You win!") 
    else:
        print("You lose!")

#Run the game
rock_paper_scissors()