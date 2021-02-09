### ARRAY LIST ###

class ArrayList:
    def __init__(self, capacity = 4):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        str_val = ""
        for i in range(self.size - 1):
            str_val += str(self.arr[i]) + ", "
        if self.size > 0:
            str_val += str(self.arr[self.size - 1])
        return str_val

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.insert(value, 0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        # Inserts an element into the array at a specific index and shifts the rest of the array
        if 0 <= index <= self.size:
            if(self.size >= self.capacity):
                self.resize()
            self.size +=1
            for i in range(self.size-1,index,-1):
                self.arr[i] = self.arr[i-1]
            self.arr[index] = value
        else:
            pass

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.insert(value, self.size)

    def count_instances(self, value):
        count = 0
        for i in range(self.size):
            if self.arr[i] == value:
                count += 1
        return count

    def resize(self):
        # Resizes the array
        self.resized_array = [0]*self.capacity*2
        for i in range(self.capacity):
            self.resized_array[i] = self.arr[i]

        self.arr = self.resized_array
        self.capacity *= 2



### RECURSION ###

def is_divisible(a, b):
    if a == b or a == 0:
        return True
    if a < 0: 
        return False
    if b == 0: 
        return False
    return is_divisible(a-b,b)


def count_matches(lis):
    if len(lis) <= 1:
        return 0
    if lis[0] == lis[1]:
        return 1 + count_matches(lis[1:])
    return count_matches(lis[1:])

### LIBRARY ###

class Book:
    def __init__(self):
        self.isbn = None
        self.name = None

    def get_isbn(self):
        return self.isbn

    def get_name(self):
        return self.name

    def set_isbn(self, ISBN):
        self.isbn = ISBN

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return f"({self.isbn}: {self.name})"

class Library:
    # I decided to go with readable instead of fast.
    def __init__(self):
        self.books = []

    def add_book(self, ISBN, name):
        for book in self.books:
            if book.get_isbn() == ISBN:
                book.set_name(name)
                return
        newbook = Book()
        newbook.set_isbn(ISBN)
        newbook.set_name(name)
        self.books.append(newbook)

    def get_book(self, ISBN):
        for book in self.books:
            if book.get_isbn() == ISBN:
                return book
        return None

    def change_book(self, ISBN, name):
        for book in self.books:
            if book.get_isbn() == ISBN:
                book.set_name(name)
        
    def remove_book(self, ISBN):
         for book in self.books:
            if book.get_isbn() == ISBN:
                self.books.remove(book)
                break

    def __str__(self):
        outstring = ""
        for book in self.books:
            outstring += f"{book}\n"
        return outstring


def inst_test(arr_lis, val):
    print("The list {" + str(arr_lis) + "} has " + str(arr_lis.count_instances(val)) + " instances of " + str(val))

def array_tests():
    print()
    print("*********ARRAY_TESTS*********:")
    print("SOME APPENDS, PREPENDS AND INSERTS")
    arr_lis = ArrayList()
    arr_lis.append(6)
    arr_lis.append(7)
    arr_lis.append(8)
    arr_lis.append(9)
    arr_lis.prepend(4)
    arr_lis.prepend(3)
    arr_lis.prepend(2)
    arr_lis.prepend(1)
    arr_lis.insert(5, 4)
    print("THE LIST: " + str(arr_lis))

    print()
    arr_lis = ArrayList()
    inst_test(arr_lis, 4)
    arr_lis.append(4)
    inst_test(arr_lis, 4)
    arr_lis.append(4)
    inst_test(arr_lis, 4)
    arr_lis.append(5)
    inst_test(arr_lis, 4)
    arr_lis.append(4)
    inst_test(arr_lis, 4)
    arr_lis.append(5)
    inst_test(arr_lis, 4)
    arr_lis.append(5)
    inst_test(arr_lis, 4)
    arr_lis.append(4)
    inst_test(arr_lis, 4)

    print()
    print("SOME INSERTS")
    arr_lis = ArrayList()
    arr_lis.insert(8, 0)
    arr_lis.insert(7, 0)
    arr_lis.insert(8, 1)
    arr_lis.insert(9, 3)
    arr_lis.insert(8, 0)
    arr_lis.insert(7, 2)
    arr_lis.insert(8, 3)
    arr_lis.insert(7, 5)
    arr_lis.insert(5, 4)
    print("THE LIST: " + str(arr_lis))

    print()
    inst_test(arr_lis, 4)
    inst_test(arr_lis, 5)
    inst_test(arr_lis, 6)
    inst_test(arr_lis, 7)
    inst_test(arr_lis, 8)
    inst_test(arr_lis, 9)

    print()
    print("SOME INSERTS")
    arr_lis = ArrayList()
    arr_lis.insert(8, -1)
    arr_lis.insert(7, 0)
    arr_lis.insert(6, 2)
    arr_lis.insert(9, 3)
    arr_lis.insert(3, 0)
    arr_lis.insert(4, 2)
    arr_lis.insert(2, 3)
    arr_lis.insert(1, 2)
    arr_lis.insert(5, 5)
    print("THE LIST: " + str(arr_lis))

    print()

def div_test(a, b):
    print("is_divisible(" + str(a) + ", " + str(b) + "): " + str(is_divisible(a, b)))

def match_test(lis):
    print("The list " + str(lis) + " has " + str(count_matches(lis)) + " matches")


def recursion_tests():
    print()
    print("*********RECURSION_TESTS*********:")
    div_test(9, 3)
    div_test(8, 2)
    div_test(8, 4)
    div_test(8, 5)
    div_test(8, 3)
    div_test(15, 7)
    div_test(14, 7)
    div_test(4, 0)
    div_test(0, 4)
    div_test(117, 9)
    print()
    match_test([0,1,2,3,4,5,6,7,8,9])
    match_test([0,1,2,2,4,5,6,6,8,9])
    match_test([0,1,2,3,5,5,5,7,8,9])
    match_test([0,1,2,3,4,5,6,7,9,9])
    match_test([0,1,3,3,3,5,6,7,7,9])
    match_test([1,1,2,2,3,3,4,4,5,5])
    match_test([0,0,0,3,4,5,5,7,8,8])
    match_test([1,1,1,3,3,5,5,5,9,9])
    match_test([])
    match_test([1,1,1,1])
    print()

#IMPORTANT: the order of the books printed does not need to match the expected output
def library_tests():
    print()
    print("*********LIBRARY_TESTS*********:")
    b1 = Book()
    b1.set_isbn("1")
    b1.set_name("Dune")
    print("testing book1:")
    print(b1)

    b2 = Book()
    b2.set_isbn("2")
    b2.set_name("At the mountains of madness")
    print("testing book2:")
    print(b2)
    
    library = Library()
    library.add_book("3", "Don Kikoti")
    print("library with 1 book:")
    print(library)
    
    library.add_book("4", "Sjálfstætt fólk")
    print("library with 2 books:")
    print(library)
    
    book = library.get_book("4")
    print("printing book with id 4")
    print(book)

    library.change_book("3", "Don Quixote")
    print("changing a diffrent book")
    print(library)

    library.add_book("3", "The trial")
    print("overwrite Don Quixote")
    print(library)

    library.remove_book("4")
    print("removed independant people")
    print(library)

if __name__ == "__main__":
    array_tests()
    recursion_tests()
    library_tests()
