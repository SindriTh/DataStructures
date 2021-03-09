class ItemExistsException(Exception):
    pass
class NotFoundException(Exception):
    pass


class BinaryTreeNode:
    def __init__(self,key = None, data = None, left = None, right = None):
        self.data = data
        self.key = key
        self.left = left
        self.right = right

class BSTMap:
    def __init__(self):
        self.root = None
        self.size = 0
    

    def insert(self,key,data):
        ''' Inserts data into the BST with a corrisponding Key'''
        self.root = self._insert_recur(self.root,key,data)

    def update(self,key,data):
        ''' Updates existing data in the BST '''
        old_node = self._find_recur(self.root,key)
        if old_node != None:
            old_node.data = data
        else:
            raise NotFoundException()
    
    def _insert_recur(self,node,key,data):
        # Insertion recursion function
        if node == None:
            self.size += 1
            return BinaryTreeNode(key,data)

        # Sets the left/right node as the outcome of this recursion which will eventually include the new node
        if node.key > key:
            node.left = self._insert_recur(node.left,key,data)
        elif node.key < key:
            node.right = self._insert_recur(node.right,key,data)
        else:
            raise ItemExistsException()
        return node


    def find(self,key):
        ''' Finds and returns the value for a specific Key '''
        # Made a variable to not have to make another function call to return
        node = self._find_recur(self.root,key)
        if node != None:
            return node.data
        raise NotFoundException()

    def contains(self,key):
        ''' Returns a boolean weather the BST contains a certain Key '''
        # Returns True if _find_recur is not none, else it returns False
        return self._find_recur(self.root,key) != None

    def _find_recur(self,node,key):
        # Search recursion function
        if node == None:
            return None
        if node.key == key:
            return node
        if node.key > key:
            return self._find_recur(node.left,key)
        if node.key < key:
            return self._find_recur(node.right,key)


    def remove(self,key):
        ''' Removes an item for a specific key '''
        self.root = self._remove_recur(self.root,key)

    def _remove_recur(self,node,key):
        # Remove recursion function
        if node == None:
            raise NotFoundException()
        elif node.key > key:
            node.left = self._remove_recur(node.left,key)
        elif node.key < key:
            node.right =  self._remove_recur(node.right,key)
        else:
            self.size -= 1
            return self._remove_node(node)
        return node

    def _remove_node(self,node):
        # Removes a specific node
        if node.left == node.right == None:
            return None
        elif node.right == None:
            return node.left
        elif node.left == None:
            return node.right
        else:
            node.right = self._swap_and_remove(node, node.right)
            return node

    def _swap_and_remove(self,starter, node):
        # Swaps the two nodes, and removes one of them. Will run again if neccesary to keep the tree correct.
        if node.left == None:
            starter.key, starter.data = node.key, node.data # Swaps the two nodes
            return self._remove_node(node)
        else:
            node.left = self._swap_and_remove(starter,node.left)
            return node

        
    def __setitem__(self,key,data):
        # Set item to enable some_bst[key] = 'something'
        # We try not to use "try" and "except" but it made a lot of sense here
        # Using Try and except leads to very legible code as well as being fast
        try:
            self.update(key, data)
        except NotFoundException:
            self.insert(key, data)

    def __getitem__(self,key):
        # Allows the syntax var = some_bst[key] to equal the search function, returning the data for the specified key
        return self.find(key)

    def __str__(self):
        return self._str_recur(self.root,"")

    def _str_recur(self,node,outstr):
        # Prints the entire tree in acending key order
        if node == None:
            return ""
        outstr += self._str_recur(node.left,outstr) + f"{{{node.key}:{node.data}}} " + self._str_recur(node.right,outstr)
        return outstr

    def __len__(self):
        # Returns the size of the dataset
        return self.size

if __name__ == "__main__":

    bss = BSTMap()
    bss.insert(4,'fa')
    bss.insert(2,'ma')
    bss.insert(3,'pa')
    bss.insert(5,'gpa')
    bss.insert(6,'gma')
    print(bss)
    bss.update(6,555)
    print(bss)
    print(bss.contains(2))
    print(bss.contains(5))
    print(bss.contains(9))
    print(bss.find(4))
    bss[4] = 'sass'
    bss[7] = 'ass'
    print(bss)
    sam = bss[4]
    print(sam)
    print('-----')
    print(bss)
    print(len(bss))
    #bss.remove(2)
    bss.remove(3)
    #bss.remove(4)
    bss.remove(6)
    bss.remove(7)
    #bss.remove(5)
    print(bss)
    print(len(bss))
