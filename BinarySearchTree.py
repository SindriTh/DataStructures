class BinaryTreeNode:
    def __init__(self,key = None, data = None, left = None, right = None):
        self.data = data
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        ret_str = ""
        if self.left != None:
            ret_str += str(self.left)
        ret_str += str(self.data) + " "
        if self.right != None:
            ret_str += str(self.right)
        return ret_str

class BST:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self,key,data):
        self.size += 1
        if self.root == None:
            self.root = BinaryTreeNode(key,data)
        else:
            self.insert_recur(self.root,key,data)
    
    def insert_recur(self,node,key,data):
        if node.key > key:
            if node.left == None:
                node.left = BinaryTreeNode(key,data)
            else:
                return self.insert_recur(node.left,key,data)

        if node.key < key:
            if node.right == None:
                node.right = BinaryTreeNode(key,data)
            else:
                return self.insert_recur(node.right,key,data)


    def contains(self,key):
        return self.find_recur(self.root,key)


    def find_recur(self,node,key):
        if node == None:
            return False
        if node.key == key:
            return True
        if node.key > key:
            return self.find_recur(node.left,key)
        if node.key < key:
            return self.find_recur(node.right,key)
   

    def remove(self,key):
        self._remove_recur(self.root,key)


    def _remove_recur(self,node,key):
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
        if node.left == None:
            starter.key = node.key
            starter.data = node.data
            return self._remove_node(node)
        else:
            node.left = self._swap_and_remove(starter,node.left)
            return node


    def __str__(self):
        return str(self.root).strip() if self.root != None else ""

    def __len__(self):
        return self.size

test = BST()
test.insert(7,'AB')
test.insert(3,'CD')
test.insert(2,'EF')
test.insert(5,'GH')
test.insert(9,'IJ')
test.insert(8,'KL')
print(test)
test.remove(3)
print(test)



def _str_recur(self,node):
    # Prints the entire tree in acending key order
    # The positioning of the fstring dictates the outcome
    outstring = ""
    if node.left != None:
        outstring += self._str_recur(node.left)
    outstring += f"{{{node.key}:{node.data}}} "
    if node.right != None:
        outstring += self._str_recur(node.right)
    return outstring