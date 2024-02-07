print("Here will be the contents of the file")
num_alines = 0
with open("x-files.txt", "r") as f:
    #inside here the f file is open for reading
    for line in f:
        num_alines += line.count("alien")

#once i am out the file is closed
print("the word alien  show up", num_alines,"times in the file")



