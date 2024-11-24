# Function to display the hash table
def display_hash(hash_table):
    for i in range(len(hash_table)):
        print(i, end=" ")
        for j in hash_table[i]:
            print("-->", j, end=" ")
        print()

# Create a hash table with 10 empty lists (buckets)
hash_table = [[] for _ in range(10)]

# Hash function to determine the index
def hashing(keyvalue):
    return keyvalue % len(hash_table)

# Function to insert a key-value pair into the hash table
def insert(hash_table, keyvalue, value):
    hash_key = hashing(keyvalue)
    hash_table[hash_key].append(value)

# Insert key-value pairs into the hash table
insert(hash_table, 10, 'Allahabad')
insert(hash_table, 25, 'Mumbai')
insert(hash_table, 20, 'Mathura')
insert(hash_table, 9, 'Delhi')
insert(hash_table, 21, 'Punjab')
insert(hash_table, 21, 'Noida')

# Display the hash table
display_hash(hash_table)
