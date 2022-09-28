def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % 100


value = get_hash('march 6')
print(value)
