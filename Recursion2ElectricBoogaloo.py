def lenofstring(strengur):
    if strengur == "":
        return 0
    return 1 + lenofstring(strengur[:-1])
    
print(lenofstring("danssn"))


def linsearch(lis,val):
    if lis == []:
        return False
    elif lis[0] == val:
        return True

    return linsearch(lis[1:],val)

lis = [0,2,4,6,7,8,9]
print(linsearch(lis,4))



def countinstances(lis,val):
    if lis == []:
        return 0
    if lis[0] == val:
        return 1 + countinstances(lis[1:],val)
    return countinstances(lis[1:],val)

lis = [0,2,4,6,7,8,9,2,3,4,2,2,2]
print(countinstances(lis,2))



def dupe(lis):
    if lis == []:
        return False
    if linsearch(lis[1:], lis[0]):
        return True
    return dupe(lis[1:])

lis = [0,2,4,6,7,8,9,10,3,11,12,13,14]
print(dupe(lis))


def removedupe(lis):
    if len(lis) == 1:
        return lis
    if linsearch(lis[1:], lis[0]):
        return removedupe(lis[1:])
    return [lis[0]] + removedupe(lis[1:])

lis = [0,2,4,6,7,8,9,10,2,11,12,13,14]
print(removedupe(lis))


def binarysearch(lis, val, first, last):
    if first > last:
        return -1

    middle = (first + last) // 2
    if val == lis[middle]:
        return middle

    if val < lis[middle]:
        return binarysearch(lis, val, first, middle-1)
    else:
        return binarysearch(lis, val, middle+1, last)

