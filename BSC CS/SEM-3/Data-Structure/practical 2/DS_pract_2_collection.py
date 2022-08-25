import collections

de = collections.deque([1, 2, 3])
print("deque: ", de)

de.append(4)

print("\nThe deque after appending at right is : ", de)

de.appendleft(6)

print("\nThe deque after appending at left is : ", de)

de.pop()

print("\nThe deque after deleting from right is : ", de)

de.popleft()
print("\nThe deque after deleting from left is : ", de)