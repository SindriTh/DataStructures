def search(lis, val, first, last):
    if first > last:
        return -1

    middle = (first + last) // 2
    if val == lis[middle]:
        return middle

    if val < lis[middle]:
        return search(lis, val, first, middle-1)
    else:
        return search(lis, val, middle+1, last)


listi = [1,2,4,6,7,8,9,12,14,15,17]
print(search(listi,15,0,len(listi)))