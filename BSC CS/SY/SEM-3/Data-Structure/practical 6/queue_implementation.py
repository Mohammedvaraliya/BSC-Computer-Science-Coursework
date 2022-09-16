import queue

q = queue.PriorityQueue()
q.put(10)
q.put(70)
q.put(30)
q.put(15)
q.put(40)
q.put(90)

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())