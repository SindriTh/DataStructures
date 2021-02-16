class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_list(head):
    if head != None:
        print(head.data, end= " ")
        print_list(head.next)
    else:
        print("")

def delete_every_other_ssl(head):
    return deo_ssl(head,0)

def deo_ssl(head,i):
    if head == None:
        return None
    
    if i%2 == 0:
        head.next = deo_ssl(head.next,i+1)
        return head
    else:
        return deo_ssl(head.next,i+1)

def linear_node_search(lis,value):
    if head == None:
        return False
    if head.data == value:
        return True
    return linear_node_search(lis[1:],value)


def merge_lists(head1,head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1

    if head1.data < head2.data:
        retNode = Node(head1.data)
        retNode.next = merge_lists(head1.next,head2)
        return retNode
    else:
        retNode = Node(head2.data)
        retNode.next = merge_lists(head1,head2.next)
        return retNode
    
#Example program:

lis1 = Node(1, Node(5, Node(6, Node(9, None))))
lis2 = Node(2, Node(7, Node(8, Node(10, None))))
lisa = merge_lists(lis1,lis2)
print_list(lisa)

head = Node("A", Node("B", Node("C", Node("D", None))))
print_list(head)
head = delete_every_other_ssl(head)
print_list(head)

# output: A B C D