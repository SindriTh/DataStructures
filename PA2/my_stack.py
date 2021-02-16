from array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    def __init__(self):
        # Pick one of these to use.
        # Stack must have the container you dont choose for Queue
        
        #self.container = LinkedList()
        self.container = ArrayDeque()
        
    # O(1)
    def push(self, data):
        self.container.push_back(data)
    
    # O(1)
    def pop(self):
        return self.container.pop_back()
    
    # O(1)
    def get_size(self):
        return self.container.get_size()

    def __str__(self):
        return ""
