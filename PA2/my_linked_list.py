class Node():
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next    # Would it not be better to call it something other than next, which is an inbuilt function?

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    # O(1)
    def push_back(self, data):
        ''' Appends the data to the linked list '''
        new_node = Node(data)
        if self._size == 0:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = self._tail.next
        self._size +=1
        return

    # O(1)
    def push_front(self,data):
        ''' Prepends the data to the linked list '''
        new_node = Node(data,self._head)
        self._head = new_node
        if self._size == 0:
            self._tail = self._head
        self._size += 1


    # O(1)
    def get_size(self):
        ''' Returns the size of the linked list '''
        return self._size

    # O(1)
    def pop_front(self):
        ''' Removes the first node of the linked list and returns it '''
        if self._head == None:
            return 

        node = self._head
        self._head = self._head.next
        self._size -= 1
        return node.data

    # O(n)
    def pop_back(self):
        ''' Removes the last node of the linked list and returns it '''
        returnnode = self._tail
        if self._tail == self._head:
            self._head, self._tail = None,None
        else:
            node = self._head
            while node.next != self._tail:
                node = node.next
            node.next = None
            self._tail = node
        
        self._size -=1
        return returnnode.data

    # O(n)
    def __str__(self):
        ''' Handles printing of the linked list '''
        node = self._head
        returnstring = ""
        while node != None:
            returnstring += str(node.data) + " "
            node = node.next
        return returnstring[:-1]


if __name__ == "__main__":
    listi = LinkedList()
    listi.push_back("1")
    listi.push_back("2")
    listi.push_front("0")
    listi.push_back("3")
    listi.push_back("4")
    print(listi)
    print(f"oh boi I popped one! {listi.pop_front()}")
    print(listi)
    print(f"Popped one from the back {listi.pop_back()}")
    print(listi)
    print(f"Popped one from the back {listi.pop_back()}")
    print(f"Popped one from the back {listi.pop_back()}")
    print(f"Popped one from the back {listi.pop_back()}")
    print(listi)