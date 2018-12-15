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

class Node(object):
    def__init__(self, data, next):
        self.data = data
        self.next = next


        



