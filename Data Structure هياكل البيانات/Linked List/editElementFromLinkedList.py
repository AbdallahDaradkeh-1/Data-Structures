class ListNode:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

# Create Linked List Nodes

node1 = ListNode(5)
node2 = ListNode(20)
node3 = ListNode(35)

# Linked Nodes together and create the head
node1.next = node2
node2.next = node3
head = node1

# Create the edit element from LinkedList:
def editElementFromLinkedList(head, index, newValue):
  temp = head
  # while we did not reach the element index and we don't reach None, continue searching
  i = 0
  while i < index and temp != None:
    temp = temp.next
    i += 1
  # if we reach None(don't find the element) return -998769
  if temp == None:
    raise ValueError("Index is out of bounds")
  else:
    temp.value = newValue
# Let us print the List as it is, then change element and print again after

# create custom print method for Linked List Elements
def LinkedListElementsPrint(head):
  temp = head
  while temp != None:
    print(temp.value)
    temp = temp.next

  

print("before")
LinkedListElementsPrint(head)
print("after")
editElementFromLinkedList(head, 2, 80)
LinkedListElementsPrint(head)





