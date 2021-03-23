class NotFoundException(Exception):
    pass
class ItemExistsException(Exception):
    pass


class Node:
    def __init__(self, key = None, data = None, _next = None):
        ''' Initializes the node class '''
        self.key = key
        self.data = data
        self.next = _next

class Bucket:
    def __init__(self):
        ''' Initializes the Bucket class '''
        self._head = None
        self._size = 0

    def insert(self, key, data):
        ''' Create a new key with data '''
        if not self.contains(key):
            self._head = Node(key,data,self._head)
            self._size += 1
        else:
            raise ItemExistsException()

    def update(self,key,data):
        ''' Updates the data of an existing item '''
        node =  self._search_recur(self._head,key)
        if node == None:
            raise NotFoundException()
        node.data = data

    def find(self,key):
        ''' Returns the data behind a specific key '''
        node =  self._search_recur(self._head,key)
        if node == None:
            raise NotFoundException()
        return node.data


    def contains(self,key):
        ''' Returns a boolean weather or not the key is found in the bucket '''
        return self._search_recur(self._head,key) != None

    def remove(self,key):
        ''' Removes a specific item from the bucket using its key '''
        if self._head == None:
            raise NotFoundException()
        elif self._head.key == key:
            self._head = self._head.next
        else:
            self._remove_recur(self._head,key)
        self._size -= 1

    def _remove_recur(self,node,keyword):
        # Recursion helper for the remove function
        if node == None or node.next == None:
            raise NotFoundException()
        if node.next.key == keyword:
            node.next = node.next.next
            return 
        return self._remove_recur(node.next,keyword)


    def _search_recur(self,node,keyword):
        # A recursion helper function that returns the node for a specific key
        if node == None:
            return
        if node.key == keyword:
            return node
        return self._search_recur(node.next,keyword)
    

    def __setitem__(self,key,data):
        ''' Allows the setitem syntax '''
        try:
            self.update(key,data)
        except NotFoundException:
            self.insert(key,data)

    def __getitem__(self,key):
        ''' Allows the getitem syntax '''
        return self.find(key)
    
    def __len__(self):
        ''' Returns the length of the bucket '''
        return self._size
        
