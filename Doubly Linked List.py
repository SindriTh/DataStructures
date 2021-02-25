class Node():
    def __init__(self,data = None, prev = None , next = None):
        self.data = data
        self.next = next
        self.prev = prev

class DLL_Deque():
    def __init__(self):
        self.header = Node()
        self.trailer = Node(None,self.header)
        self.header.next = self.trailer

    def push_front(self,data):
        new_node = Node(data,self.header,self.header.next)
        self.header.next.prev = new_node
        self.header.next = new_node

    def pop_front(self):
        if self.header.next is self.trailer:
            return

        returnnode = self.header.next
        returnnode.next.prev = self.header
        self.header.next = returnnode.next
        return returnnode.data


    def push_back(self,data):
        pass
    
    def pop_back(self):
        pass

    def __str__(self):
        node = self.header.next
        outstring = ""
        while node is not self.trailer:
            outstring += (str(node.data)) + " "
            node = node.next
        return outstring[:-1]

    def print_reversed(self):
        node = self.trailer.prev
        outstring = ""
        while node is not self.header:
            outstring += (str(node.data)) + " "
            node = node.prev
        return outstring[:-1]


class DLL_Poslist():
    def __init__(self):
        self.header = Node()
        self.trailer = Node(None,self.header)
        self.header.next = self.trailer
        self.curr = self.trailer
    
    def insert(self,data):
        node = Node(data,self.curr.prev,self.curr)
        self.curr.prev.next = node
        self.curr.prev = node

    def __str__(self):
        node = self.header.next
        outstring = ""
        while node is not self.trailer:
            outstring += (str(node.data)) + " "
            node = node.next
        return outstring[:-1]



if __name__ == "__main__":
    deque = DLL_Deque()
    deque.push_front(23)
    deque.push_front(3)
    deque.push_front(15)
    deque.push_front(65)
    print(deque)
    print(deque.print_reversed())
    print(deque.pop_front())
    print(deque.pop_front())
    print(deque.pop_front())
    print(deque.pop_front())
    print(deque.pop_front())
    print(deque.pop_front())
    print(deque.pop_front())

    print(str(deque))