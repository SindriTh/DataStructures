class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    # O(1)
    def __init__(self):
        ''' Initializes the Doubly Linked List '''
        self.clear()
        self.counter = 0

    # O(1)
    def insert(self, data):
        ''' Inserts data at the current index '''
        if self._size <= 0:
            node = Node(data,self._header,self._trailer)
            self._trailer.prev = node
            self._header.next = node
        else:
            node = Node(data,self._curr.prev,self._curr)
            self._curr.prev.next = node
            self._curr.prev = node

        self._curr = node
        self._size += 1

    # O(1)
    def remove(self):
        ''' Removes the current index '''
        if self._curr.data != None and self._size > 0:
            self._size -= 1
            self._curr.next.prev = self._curr.prev
            self._curr.prev.next = self._curr.next
            self._curr = self._curr.next
            

    # O(1)
    def get_value(self):
        ''' Returns the data in the current index '''
        return self._curr.data

    # O(1)
    def move_to_next(self):
        ''' Moves the current index forwards '''
        if self._curr.data != None and self._curr.next != None:
            self._curr = self._curr.next

    # O(1)
    def move_to_prev(self):
        ''' Moves the current index backwards '''
        if self._curr.prev != None:
            if self._curr.prev.data != None:
                self._curr = self._curr.prev

    # O(n)
    def move_to_pos(self, pos):
        ''' Moves the current index to a specific location '''
        if 0 <= pos <= self._size:
            counter = 0
            node = self._header.next
            while node.data != None and counter <= pos:
                node = node.next
                counter += 1
            self._curr = node.prev
        if pos == self._size:
           self._curr = node

    # O(1)
    def clear(self):
        ''' Clears the list '''
        self._header = Node()
        self._trailer = Node(None,self._header)
        self._header.next = self._trailer
        self._curr = self._trailer
        self._size = 0

    # O(1)
    def get_first_node(self):
        ''' Returns the first node '''
        return self._header.next

    # O(1)
    def get_last_node(self):
        ''' Returns the last node '''
        return self._trailer.prev

    # O(n)
    def partition(self, low, high):
        ''' Partitions the list from low to high '''
        # "low" variable is the pivot and then the function parses through the list
        # If the data at the current index is smaller than the pivot, it moves the indexed value to the one in front of the pivot
        self._curr = low.next
        while self._curr != high.next:
                if self._curr.data < low.data:
                    newnode = Node(self._curr.data,low.prev,low)
                    low.prev.next = newnode
                    low.prev = newnode
                    self._size += 1 # Fixes the size reduction that happens in the remove function
                    self.remove()
                else:
                    self._curr = self._curr.next
        self._curr = low

    # O(n^2)
    def sort(self):
        ''' Sorts the list '''
        if self._header.next != self._trailer:
            self._curr = self.get_first_node()
            while self._curr.next != None:
                indexer = self._curr.next
                while indexer.data != None:
                    if self._curr.data > indexer.data:
                        data = self._curr.data
                        self._curr.data = indexer.data
                        indexer.data = data

                    indexer = indexer.next

                self._curr = self._curr.next
                
            self._curr = self.get_first_node()
            

    # O(1)
    def __len__(self):
        ''' Returns the length of the linked list '''
        return self._size

    # O(n)
    def __str__(self):
        ''' Returns all the elements of the linked list '''
        node = self._header.next
        out_string = ""
        while node is not self._trailer:
            out_string += (str(node.data)) + " "
            node = node.next
        return out_string[:-1]

if __name__ == "__main__":
    #create tests here if you want
    dll = DLL()
    dll.insert(25)
    dll.insert(30)
    dll.insert(35)
    dll.insert(40)
    dll.insert(45)
    dll.insert(8)
    dll.insert(19)
    dll.insert(26)
    dll.insert(48)
    dll.insert(91)
    dll.insert(23)
    dll.insert(85)
    dll.insert(59)
    dll.insert(69)
    dll.insert(110)
    dll.insert(203)
    dll.insert(5)
    dll.insert(49)
    #print(dll)
    #dll.partition(dll.get_first_node(),dll.get_last_node())
    #print(dll.get_value())
    #dll.move_to_next()
    #dll.move_to_next()
    #print(dll.get_value())
    print(dll)
    dll.sort()
    print(dll)
    dll.move_to_pos(8)
    print(dll.get_value())
    print(dll)
    print(len(dll))
    print("------------")
    dll.move_to_pos(len(dll)-1)
    dll.remove()
    print(dll.get_value())
    print(len(dll))
    print(dll)
