pq = []

pq.append((2, "A"))
pq.append((3, "B"))
pq.append((1, "C"))
pq.append((7, "D"))

print(pq)

pq.sort()
print(pq)

print(pq.pop())
print(pq.pop())
print(pq.pop())
print(pq.pop())

print(pq)
