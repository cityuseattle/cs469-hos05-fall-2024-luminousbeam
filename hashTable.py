class HashTable:
  def __init__(self) -> None:
    self.size = 11
    self.slots = [None] * self.size
    self.data = [None] * self.size

  def put(self, key, data):
    # Calculate the hash value, aka the index for the key in the hash
    hash_value = self.hash(key, len(self.slots))

    # If current slot is empty, assign/insert the key and data
    if self.slots[hash_value] == None:
      self.slots[hash_value] = key
      self.data[hash_value] = data
    # If there is a key occupying the slot
    else:
      # If the key is the same as the key in the slot, update the data
      if self.slots[hash_value] == key:
        self.data[hash_value] = data
      # If the key is different...
      else:
        next_slot = self.rehash(hash_value, len(self.slots))
        # Try to find the next available slot with the same key
        while self.slots[next_slot] != None and self.slots[next_slot] != key:
          next_slot = self.rehash(next_slot, len(self.slots))

        if self.slots[next_slot] == None:
          self.slots[next_slot] = key
          self.data[next_slot] = data
        else:
          self.data[next_slot] = data

  def hash(self, key, size):
    # Calculate the hash value using a remainder method
    return key % size

  def rehash(self, old_hash_value, size):
    return (old_hash_value + 1) % size

  def get(self, key):
    start_slot = self.hash(key, len(self.slots))
    data = None
    stop = None
    found = False
    position = start_slot

    while self.slots[position] != None and not found and not stop:
      if self.slots[position] is key:
        found = True
        data = self.data[position]
      else:
        position = self.rehash(position, len(self.slots))
        if position is start_slot:
          stop = True
    return data

  def __getitem__(self, key):
    return self.get(key)

  def __setitem__(self, key, data):
    self.put(key, data)

# Test
H = HashTable()

# Store items with int keys and str data
H[22] = 'cat'
H[26] = 'dog'
H[93] = 'lion'
H[17] = 'tiger'

print("data: ", H.data)
print("slots: ", H.slots)

# Modify the hash table
print(H[22])
H[22] = 'duck'
print(H[22])

print("Hash Table:")
print("Index | Key   | Value")
print("---------------------")
for index in range(H.size):
    print(f"{index:5} | {str(H.slots[index]):5} | {str(H.data[index]):5}")
