class listNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next



node1 = listNode(5)

node2 = listNode(10)

node3 = listNode(20)

head = node1

node1.next = node2
node2.next = node3
temp = head
for i in range(3):
    if temp == head:
        print(temp.value)
        temp = temp.next
    else:
        print(temp.value)
        temp = temp.next
