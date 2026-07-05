class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next




# First Case: Adding an element to a Linked List that is empty (does not have any elements)




def addElementToLinkedList(head, value):
    newNode = ListNode(value)
    temp = head
    if(head == None):
        head = newNode
    else:
        while temp.next != None:
            temp = temp.next
        temp.next = newNode
    return head




# right now there is no Linked List, so head is not pointing to any node/element, so head is None

head = None
head = addElementToLinkedList(head, 5)
print(head.value)
head = addElementToLinkedList(head, 10)

i = 2
temp = head
for i in range(2):
    print(temp.value)
    temp = temp.next

    