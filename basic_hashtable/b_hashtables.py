

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.elements = [None] * capacity
        pass

    # '''
    # Fill this in.
    # Research and implement the djb2 hash function
    # '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = ((hash << 5) + hash) + ord(x)
        print("x is: ",x)
        print("hash is: ",hash)
    hash_val = hash % max & 0xFFFFFFFF
    return hash_val

    # '''
    # Fill this in.

    # If you are overwriting a value with a different key, print a warning.
    # '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    pair = Pair(key, value)
    if hash_table.elements[index] is not None:
        print(f"You are overwriting element '{hash_table.elements[index]}' at index '{index}' with value '{value}'")
    print('hash_table.elements[index] was: ', hash_table.elements[index])
    hash_table.elements[index] = pair
    print('index is: ',index)
    print('value is: ',value)
    print('hash_table.elements[index] is now: ', hash_table.elements[index])

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    pair = Pair(key, value)
    if hash_table.elements[index] is not None:
        print(f"You are overwriting element '{hash_table.elements[index]}' at index '{index}' with value '{value}'")
    print('hash_table.elements[index] was: ', hash_table.elements[index])
    hash_table.elements[index] = pair
    print('index is: ', index)
    print('value is: ', value)
    print('hash_table.elements[index] is now: ', hash_table.elements[index])


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    pass


def Testing():
    ht = BasicHashTable(16)
    print('hash is: ',hash("Grace Hopper", ht.capacity))
    hash_table_insert(ht, "2384729842", "Grace Hopper")
    hash_table_insert(ht, "2384729842", "John McCarthy")
    print('elements are: ',ht.elements)
    # hash_table_remove(ht, "line")
    #
    # if hash_table_retrieve(ht, "line") is None:
    #     print("...gone tomorrow (success!)")
    # else:
    #     print("ERROR:  STILL HERE")


Testing()





# print(hash("Hedera Hashgraph", 16))