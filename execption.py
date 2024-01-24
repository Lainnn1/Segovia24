
try:
    age1 = int(input("What is your age P1?"))
    age2 = int(input("What is your age P2"))
    res = age1/age2
except ValueError:
    print("I am sorry but that is not a valid number")
else:
    print("Player 1 is older than player 2 by a factor of",res)
