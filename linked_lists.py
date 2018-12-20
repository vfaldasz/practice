#2.1 Remove the duplicate values from a linked list.
def remove_duplicates(self, head):

    current = self.head #start at the head
    if current: # if linked list is not empty
        dict = {current.data: True} # add current to dict
        while current.next: #if next value is not None
            if current.next.data in dict:
                current.next = current.next.next
            else:
                dict[current.next.data] = True
                current = current.next
    return head
#_________________________________________

#building appending and extending method for LL
class Node(object):
    def__init__(self, data, next):
        self.data = data
        self.next = next

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedList():
    def __init__(self):
        self.head = None

    def append(self, val):
        n= Node (val):
        current = self.head
        if current is None:
            self.head = n
            return
        while current.next:
            current = current.next
        current.next = n

    def extend(self, lst):
        current = self.head
        while current and current.next:
            current = current.next
        for item in lst:
            n = Node (item)
            if self.head is None:
                self.head = n
                current = n
            else:
                current.next = n
                current = current.next

#_________________________________________________

#create method that reverses a linked_list (Dec 17)

def reverse_ll(self):
    current = self.head
    while current:
        next_node = current.next
        if self.head == current:
            current.next = None
        else: 
            current.next = self.head
            self.head = current
        current= next_node

#________________________________________________

#create method that finds length (counts number) in linked list

def length(self):

    count = 0
    current = self.head

    while current:
        count +=1
        current = current.next

    return count





