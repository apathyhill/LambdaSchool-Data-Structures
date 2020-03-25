from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.storage = DoublyLinkedList()
        self.storage_dict = {}


    def move_to_front(self, key, last_key):
        self.storage_dict[key] = 0
        for i in self.storage_dict:
            if self.storage_dict[i] < last_key:
                self.storage_dict[i] += 1
            if self.storage_dict[i] >= self.limit:
                self.storage.remove_from_tail()
                self.storage_dict.pop(i)

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.storage_dict: # Check if key exists
            return None
        node = self.storage.head # Start at head, and go until none left
        while node:
            if self.storage_dict[key] == node: # If key's value is the current node
                self.storage.move_to_front(node) # Move to head
                self.storage_dict[key] = self.storage.head # Update key to head
                return self.storage_dict[key].value
            node = node.next # Get next node
        return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage_dict: # Delete if exists
            self.storage.delete(self.storage_dict[key])
        
        self.storage.add_to_head(value) # Add value to head and add to the dict
        self.storage_dict[key] = self.storage.head

        while len(self.storage) > self.limit: # Cleanup if size > limit
            node = self.storage.tail
            keys = list(self.storage_dict.keys())
            for i in keys:
                if self.storage_dict[i] == node:
                    self.storage_dict.pop(i)
                    break
            self.storage.remove_from_tail()