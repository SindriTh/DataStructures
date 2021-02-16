class Node():
    def __init__(self,data = None,nexxt = None):
        self.data = data
        self.next = nexxt

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def push_back(self, data):
        new_node = Node(data)
        if self._head == None:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node

    def push_front(self,data):
        new_node = Node(data,self._head)
        self._head = new_node

    def __str__(self):
        node = self._head
        returnstring = ""
        while node != None:
            returnstring += str(node.data) + "\n"
            node = node.next
        return returnstring



listi = LinkedList()
listi.push_back("1")
listi.push_back("2")
listi.push_front("0")
print(listi)







def push_front(head, data):
    new_node = Node(data,head)
    return new_node

def print_list(head):
    if head != None:
        print_list(head.next)
        print(head.data)

head = Node()
head.data = "String 1"
for i in range(2,6):
    head = push_front(head,f"String {i}")



print_list(head)

# node = head
# while node != None:
#     print(node.data)
#     node = node.next
