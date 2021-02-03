import random

goal = random.randint(1, 100)

while True:
    s = input("Enter a number: ")
    if not s.isdigit():
        continue
    n = int(s)
    if goal > n:
        print("Too small")
    elif goal < n:
        print("Too big")
    else:
        print("Got it :)")
        break
    
