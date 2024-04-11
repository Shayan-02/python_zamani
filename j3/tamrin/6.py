import random


while True:
    user = input("enter a choice\nrock\npaper\nscissors\nfor exit ---> payan\n: ")
    computer = random.choice(["rock", "paper", "scissors"])
    if user == computer:
        print("it's a tie")
    elif user == "rock":
        if computer == "scissors":
            print(f"computer choosed {computer} user choosed {user} so user win")
        else:
            print(f"computer choosed {computer} so user lose")
    elif user == "paper":
        if computer == "rock":
            print(f"computer choosed {computer} so user win")
        else:
            print(f"computer choosed {computer} so user lose")
    elif user == "scissors":
        if computer == "paper":
            print("user win")
        else:
            print(f"computer choosed {computer} so user lose")
    if user == "payan":
        break
