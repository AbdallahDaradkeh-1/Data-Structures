class ListNode:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

def removeElementFromLinkedList(head, value):
  temp = head
  q = None
  
  while temp != None and temp.value != value:
    q = temp
    temp = temp.next
  if temp == None:
    print("Element does not exist")
  else:
    if temp == head:
      head = head.next
      return head
    else:
      q.next = temp.next
    

node1 = ListNode(5)
node2 = ListNode(10)

head = node1
node1.next = node2

node3 = ListNode(15)
node2.next = node3

# Print All Elements of LinkedList

removeElementFromLinkedList(head, 15)
removeElementFromLinkedList(head, 10)
head = removeElementFromLinkedList(head, 5)

temp = head

while temp != None:
  print(temp.value)
  temp = temp.next
print('No Element')



