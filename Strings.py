hi = "hello"
print(hi[0])

print(hi[-1])

print(hi[1])

bye = "bye"

print(bye+hi)

print(3*hi)

#the built in function len() will return the lenght of a string. This is a general function that can be used with other non scalar objects
print(5*hi)
print(len(hi))

base = "abcdefghijklmnopqrstuvwxyz"
print("here are some slices")
print(base[0:3])
print(base[10:])  # all the way till the end
print(base[:10])  # all the way from the beginning
print(base[:])  # the whole string

print(base[::2])  # every other letter
print(base[5:15:3])  # from 5th character to the 14th, in steps of 3
print(base[::-1])  # the whole string backwards