try:
    age = int(input('How old are you? '))
    country = input('Where do you live')
except ValueError:
    print("I am sorry, but that is not a valid number.")
else:
    if age < 0 or age > 130 :
        print("I am sorry, but your age cannot be negative, or greater than 130.")
    elif age < 18:
        print("You are too young to play this game")
    elif age < 21 and country == "US" :
        print ("I am sorry but you are too young to play this game in the US")

    else:
        print("take a shot of tequila. Thank you for playing")