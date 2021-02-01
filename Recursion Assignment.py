def less_than(a,b):
    ''' Checks if the first number is less than the second one '''
    if a == 0 and b != 0:
        return True
    elif b == 0:
        return False
    return less_than(a-1,b-1)



def unique(lis):
    # I decided to use a helper in case we would want to check user input before running the recursive check.
    # This would be the place for that.
    ''' Returns a new list of unique elements of a list '''
    uniquelis = []
    return unique_helper(lis,uniquelis)

def unique_helper(lis1,unique_list):
    if len(lis1) == 0:
        return unique_list
    if not unique_linear_search_helper(unique_list,lis1[0]):
        unique_list.append(lis1[0])
    unique_helper(lis1[1:],unique_list)
    return unique_list

def unique_linear_search_helper(lis,val):
    # Linear search through the unique list
    if lis == []:
        return False
    elif lis[0] == val:
        return True
    return unique_linear_search_helper(lis[1:],val)

print(unique([0,1,2,3,3,4,5,5]))