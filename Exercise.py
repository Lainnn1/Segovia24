#iterate over a string backwards using while

text = "abcdefg"
print(text)
i= -1
while i >= -7:
    print(text[i])
    i -=  1


print(text)
i= 0
while i < len(text):
    print(text[len(text)-1-i])
    i +=  1


base = "abcdefghijklmnopqrstuvwxyz"

print("here are some slices")
print(base[0:3])
#from position 10 all the way till the end
print(base[10:])
#all the way from the beginning until position 10
print(base[:10])
#every other letter
print(base[::2])
#every third letter from the 5th to the 15th
print(base[5:15:3])
#the whole string backwards
print(base[::-1])

#use double equal sign (==) to compare if 2 strings are the same
hi= "banana"
print (hi == "banana")
print (hi == "Banana")
print(hi > "bana")
print(hi < "ZZZ")
