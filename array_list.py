class IndexOutOfBounds(Exception):
    pass

class Empty(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.__reset()

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        ''' Returns a string of all array elements '''
        return_string = ""
        for i in range(self.size):
            return_string += f"{self.array[i]}"
            return_string += ", " if i < self.size-1 else ""
        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        ''' Prepends an element to the array '''
        self.insert(value,0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        ''' Inserts an element into the array at a specific index and shifts the rest of the array'''
        if 0 <= index <= self.size:
            if(self.size >= self.capacity):
                self.resize()
            self.size +=1
            for i in range(self.size-1,index,-1):
                self.array[i] = self.array[i-1]
            self.array[index] = value
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def append(self, value):
        ''' Appends an element to the array '''
        # I can call the insert method in O(1) because the for loop will never run no matter the array size.
        self.insert(value,self.size)
        
        # In case teachers dont like my reasoning this would work too, but is repeated code.
        #if(self.size >= self.capacity):
        #    self.resize()
        #self.array[self.size] = value
        #self.size +=1
        

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        ''' Inserts an element into the array at a specific index and overwrites the current value'''
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def get_first(self):
        ''' Returns the first element of the array '''
        if self.size != 0:
            return self.array[0]
        raise Empty()
        

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        ''' Returns an element from a specific index in the array '''
        if self.size > index >= 0:
            return self.array[index]
        raise IndexOutOfBounds()
        

    #Time complexity: O(1) - constant time
    def get_last(self):
        ''' Returns the last element of the array '''
        if self.size != 0:
            return self.array[self.size-1]
        raise Empty()


    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        ''' Resizes the array '''
        # I dont see a way to expand the list other than to create a new one and then replacing the existing one with the newly created one.
        self.resized_array = [0]*self.capacity*2
        for i in range(self.capacity):
            self.resized_array[i] = self.array[i]

        self.array = self.resized_array
        self.capacity *= 2
        

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        ''' Removes an element at a specific index of the array '''
        if 0 <= index < self.size:
            self.size -=1
            for i in range(index,self.size):
                self.array[i] = self.array[i+1]
        else:
            raise IndexOutOfBounds()
    #Time complexity: O(1) - constant time
    def clear(self):
        ''' Clears the array '''
        self.__reset()

    #Time complexity: O(1) - constant time
    def __reset(self):
        # Empties the array and resets its size.
        self.size = 0
        self.capacity = 4
        self.array = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of sublist
    def sublist(self, start, length):
        ''' Creates a sublist of length "length" starting from index "start" '''
        if length+start > self.size or start < 0:
            raise IndexOutOfBounds()
        sublist = ArrayList()
        return self.__sublist_recursion(sublist,start,length)
        

    def __sublist_recursion(self,subarray,start,length):
        # Recursion helper method
        if length == 0:
            return subarray

        self.__sublist_recursion(subarray,start,length-1)
        subarray.append(self.array[start+length-1])
        return subarray


    #Time complexity: O(n) - linear time in size of concatinated list
    # OR
    #Time complexity: O(n+m) - linear time in size of both lists, self and other
    def concatenate(self, other):
        ''' Concatinates two arrays and returns a new array'''
        array = ArrayList()
        self.__concat_recursion(array,self.size,self.array)
        return self.__concat_recursion(array,other.size,other.array)
         

    def __concat_recursion(self,lis,length,myarray):
        # Recursion helper method
        if length == 0:
            return lis

        self.__concat_recursion(lis,length-1,myarray)
        lis.append(myarray[length-1])
        return lis



if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    #print(str(arr_lis))

    arr_lis.prepend('epli')
    print(str(arr_lis))
    arr_lis.prepend(1)
    print(str(arr_lis))
    arr_lis.append(3)
    print(str(arr_lis))
    arr_lis.append(4)
    print(str(arr_lis))
    arr_lis.append(5)
    print(str(arr_lis))
    arr_lis.prepend(0)
    print(str(arr_lis))
    arr_lis.set_at(10,2)
    print(str(arr_lis))
    arr_lis.insert(2,2)
    print(str(arr_lis))
    arr_lis.remove_at(3)
    print(str(arr_lis))
    print(arr_lis.get_first())
    arr_lis.prepend(2)
    print(str(arr_lis))
    arr_lis.prepend(1)
    print(str(arr_lis))
    arr_lis.append(3)
    print(str(arr_lis))
    arr_lis.append(4)
    print(str(arr_lis))
    
    arr2 = arr_lis.sublist(4,5)

    print(arr_lis.concatenate(arr2))
