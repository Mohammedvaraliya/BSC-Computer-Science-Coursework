import hashlib
result = hashlib.md5(b'MVLU')
result1 = hashlib.md5(b'mvlu')
# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end ="")
print(result.digest())
print("The byte equivalent of hash is : ", end ="")
print(result1.digest())