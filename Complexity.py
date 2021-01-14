import random
# O(1)
def BigO1example():
    n = 1000000
    return "Hello World"

#O(log(n))
# If we do a binary search on an ordered list. We get O(log2(n))
def BigOlogexample():
    n = 1000000000
    a = 0
    while n > 1:
        a += 1
        n //= 2
    print(a)


# O(n)
def bigOexample():
    n = 100000  # O(1)
    a = 0       # O(1)
    a = a + 1   # O(1)
    for i in range(n): # O(n)
        a = a + 1

#O(n^2)
def bigON2example():
    n = 100000  # O(1)
    a = 0       # O(1)
    a = a + 1   # O(1)
    for i in range(n): # O(n)
        for j in range(n): # O(n)
            a = a + 1


##########
# Time complexity and lists


# O(n) where n is the second_parameter
def mathfunction(first_param, second_param):
    if second_param <= 0:
        return
    total = 1               # O(1)
    for i in range(0,second_param): #O()
        total *= first_param
    return total


#O(n) where n is the parameter b
def multiplicationofpositiveintegers(a,b):
    total = 0
    for i in range(b):
        total += a
    return total

#O(n) where n is the size of the list.
def randomnumberinsertion(size):
    lis = [0]*size
    for i in range(size):
        lis[i] = random.randint(1,6)    # Lets assume its O(1)


def printlist(lis):
    for i in lis:
        print(i,end=" ")
    # Wierd project description, Skipping for now


# C(1)
def increseatrandom(lis):
    randomint = random.randint(0,len(lis)-1)
    lis[randomint] +=1
    return lis


def switchtwo(lis):
    ind1 = random.randint(0,len(lis)-1)
    ind2 = random.randint(0,len(lis)-1)

    temp = lis[ind1]
    lis[ind1] = lis[ind2]
    lis[ind2] = temp
    return lis

print(switchtwo([0,1,2,3,4,5,6,7,8,9]))