

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
        # print("x is: ",x)
        # print("hash is: ",hash)
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
        print(f"You are overwriting element '{str(hash_table.elements[index].value)}' at index '{index}' with value '{value}'")
    # print('hash_table.elements[index] was: ', hash_table.elements[index])
    hash_table.elements[index] = pair
    # print('index is: ',index)
    # print('value is: ',value)
    # print('hash_table.elements[index] is now: ', hash_table.elements[index].value)

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    # pair = Pair(key, value)
    val = 0
    if hash_table.elements[index] is None:
        print(f"No value found at index {index}")
    elif hash_table.elements[index] is not None:
        val = hash_table.elements[index].value
        print('hash table elements: ',hash_table.elements)
        print('ht element length was: ',len(hash_table.elements))
        print('found val: ',hash_table.elements[index].value)
        del hash_table.elements[index]
        print('ht element length is now: ',len(hash_table.elements))
        print('hash table elements: ',hash_table.elements)
        # for i in range(index, hash_table.capacity):
        #     hash_table.elements[i - 1] = hash_table.elements[i]
    return val

    # hash_table.elements[index] = pair



'''
Fill this in.

Should return None if the key is not found.
'''
def hash_table_retrieve(hash_table, key):
    pass


def Testing():
    ht = BasicHashTable(16)
    # print('hash is: ',hash("Grace Hopper", ht.capacity))
    hash_table_insert(ht, "2384729842", "Dapper Dan")
    hash_table_insert(ht, "2384729842", "Virgil Abloh")
    element_list = []
    for x in ht.elements:
        if x is None:
            element_list.append(x)
        elif x is not None:
            element_list.append(x.value)
    print('ele_list: ',element_list)
    hash_table_remove(ht, "2384729842")
    #
    # if hash_table_retrieve(ht, "line") is None:
    #     print("...gone tomorrow (success!)")
    # else:
    #     print("ERROR:  STILL HERE")


Testing()





# print(hash("Hedera Hashgraph", 16))