# Create LinkedList

class ListNode:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

# Before We have any Node, head is pointing to nothing
head = None

# Add Element to a Linked List Method
def addElementToLinkedList(head, value):
  # Create the Node with the value you want to add
  node = ListNode(value)
  temp = head
  # Add the element at the first(if the LinkedList is empty)
  if(head == None):
    head = node
    return head
  else:
    # If Linked List contains elements, add the Node at the end
    while temp.next != None:
      temp = temp.next
    temp.next = node
    return head # return head because python somtimes does not update the head
# Test the add Method
head = addElementToLinkedList(head, 5)
head = addElementToLinkedList(head, 11)

# Print Method
def printLinkedListElements(head):
  temp = head
  while temp != None:
    print(temp.value)
    temp = temp.next
# Print Linked List Elements
printLinkedListElements(head)

# Get Element From Linked List Function
def getElementFromLinkedListFunction(head, index):
  temp = head
  # traverse until we reach index or reached the end of the List so(not exist/out of bounds)
  i = 0
  while i < index and temp != None:
    temp = temp.next
    i += 1
  if temp != None:
    return temp.value
  else:
    return 0 # Element is not exist
# Test The function
targetElement = getElementFromLinkedListFunction(head, 0)
print("Target: ", targetElement)

# RemoveElementFromLinkedList Method
def removeElementFromLinkedList(head, value):
  temp = head
  q = None

  while temp != None and temp.value != value:
    q = temp
    temp = temp.next
  if temp == None:
    return 0
  else:
    if temp == head:
      head = head.next
      return head # Return head because python does not update it in its own
    else:
      q.next = temp.next
# Test the remove method
print("after")
head =removeElementFromLinkedList(head, 5)
printLinkedListElements(head)

