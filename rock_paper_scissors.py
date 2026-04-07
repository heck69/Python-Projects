import random

while True:
    
    print("Welcome to Rock, Paper, Scissors!")

    u_choice= int(input("Enter choice - \n 1. Rock \n 2. Paper \n 3. Scissors \n"))

    while not u_choice >= 1 and u_choice <= 3:
        u_choice = int(input("not in range, try again: "))

    if u_choice == 1:
        u_name = 'Rock'
    elif u_choice == 2:
        u_name = 'paper'
    elif u_choice == 3:
        u_name = 'scissors'

    print(f"User Choice : {u_choice},{u_name}")

    print("computer turn...")

    c_choice = random.randint(1,3)

    if c_choice == 1:
        c_name = 'Rock'
    elif c_choice == 2:
        c_name = 'paper'
    elif c_choice == 3:
        c_name = 'scissors'

    print(f"Computer Choice is : {c_choice}, {c_name}")

    print (f"USER : {u_name} vs COMP : {c_name}")

    if u_choice == c_choice:
        result = 'DRAW'
    elif (u_choice == 1 and c_choice == 2) or (c_choice == 1 and u_choice == 2):
        result = 'paper'
    elif (u_choice == 1 and c_choice == 3) or (c_choice == 1 and u_choice == 3):
        result = 'Rock'
    elif (u_choice == 3 and c_choice == 2) or (c_choice == 3 and u_choice == 2):
        result = 'scissors'
        

    if result == 'DRAW':
        print("---TIE---")
    elif result == u_name:
        print("--USER WINS--")
    elif result == c_name:
        print("--COMPUTER WINS--")

    ans = input("Want to play again?[Y/N]: ").lower()

    if ans == 'n':
        break

print("Thank you")