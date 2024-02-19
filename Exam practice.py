print (2!=3)#bool
6/2 #float
5 or 6 # int
print #function
print(2*2) #nonetype
"abc".find #method
"bubu"*2 #string
print(2+3*2**2)
("abc",2)#list
[1,2,3].append("John") #string
"bubu"*2 #string
print(type("bubu"*2))
def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
