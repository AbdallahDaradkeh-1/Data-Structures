class Queue:
  def __init__(self):
    self.q = []
  
  def enqueue(self, element):
    self.q.append(element)
  
  def dequeue(self):
    if self.isEmpty():
      print("Error")
    else:
      self.q.pop(0)

  def printQueue(self):
    qLength = len(self.q)
    i = 0
    while i < qLength:
      print(self.q[i])
      i +=1
  def front(self):
    if self.isEmpty():
      print("Error")
      return None
    else:
      return self.q[0]

  def isEmpty(self):
    if len(self.q) == 0:
      return True
    else:
      return False


queue1 = Queue()

queue1.enqueue(5)
queue1.enqueue(10)
queue1.enqueue(15)
queue1.enqueue(20)
queue1.enqueue(25)

queue1.dequeue()

queue1.printQueue()

print("front", queue1.front())