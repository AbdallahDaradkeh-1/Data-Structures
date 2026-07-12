class Stack:
  def __init__(self):
    self.s = []
    
  def push(self, element):
    self.s.append(element)
  def printStack(self):
    sLength = len(self.s)
    i = 0
    while i < sLength:
      print(self.s[i])
      i += 1
  def pop(self):
    if self.isEmpty():
      print("Error")
    else:
      self.s.pop()
  def top(self):
    if self.isEmpty():
      print("Array is empty, there are no Elements")
      return None
    else:
      return self.s[-1]
  def isEmpty(self):
    if len(self.s) == 0:
      return True
    else:
      return False
  
stack1 = Stack()
stack1.push(5)
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.top()

stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.printStack()
print("Top" ,stack1.top())