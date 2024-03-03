f = open("x-files.txt", "w")
while True:
    line = input("Give me text to put into a file: ")
    if line.lower() == "stop":
        break
    f.write(line + "\n")

# closes file
f.close()


import random
def greet():
    """
    This is a basic function used for teaching.
    It just prints two lines of text.
    """
    print("Hello, World!")
    print("Bye World!")
    return 7

def operation_threenum(a,b,c):


    return a * b + c



def read_threenum(e=0,f=0,g=0):
    """
    This function reads 3 numbers from the user
    :return: The 3 numbers
    """
    e = int(input("Enter first: "))
    f = int(input("Enter second: "))
    g = int(input("Enter third: "))
    return e, f, g

print(operation_threenum(a = 3, b = 7, c = 10))

zulu = read_threenum()
print(zulu[0] * zulu[2])