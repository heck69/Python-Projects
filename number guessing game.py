import random

low = int(input("Lower Bound: "))
high = int(input("Upper Bound: "))

num = random.randint(low, high)

tc = 7
ch = 0

while ch < tc:
    ch += 1
    g = int(input(f"Enter Guess {ch}:"))

    if g == num:
        print(f"Correct, guessed in {ch} guesses")
        break
    if g > high or g < low:
        print("guess not in range")
    if ch == tc and g != num:
        print(f"num was {num}")
    elif g>num and (g < high and g > low):
        print("high")
    elif g<num and (g < high and g > low):
        print("low")
    