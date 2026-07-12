class ListNode:
  def __init__(self, value, next = None):
    self.value = value
    self.next = None

# Scroll down to find Get Element From Linked List Function

def addElementToLinkedList(head, value):
  node = ListNode(value)
  temp = head
  if(head == None):
    head = node
  
  else:
    while temp.next != None:
      temp.next
    temp.next = node
  return head

head = None
head = addElementToLinkedList(head, 5)
head = addElementToLinkedList(head, 10)


def getElementFromLinkedList(head, index):
  temp = head
  i = 0
  while i < index and  temp != None:
    temp = temp.next
    i += 1
  if temp != None:
    return temp.value
  else:
    return "element is not exist"
  
# Let us test the Function

target = getElementFromLinkedList(head, 1)

print("target ", target)




temp = head

while temp != None:
  print(temp.value)
  temp = temp.next


