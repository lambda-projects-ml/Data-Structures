# class Queue:
#     def __init__(self):
#         self.size = 0
#         # what data structure should we
#         # use to store queue elements?
#         self.storage = []

#     def enqueue(self, item):
#         self.storage.append(item)

#     def dequeue(self):
#         if len(self.storage) == 0:
#             return None
#         else:
#             return self.storage.pop(0)

#     def len(self):
#         return len(self.storage)


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def get_next(self):
        return self.next_node

    def get_value(self):
        return self.value


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail = new_node
            self.tail.set_next(new_node)
            self.size += 1

    def dequeue(self):
        if not self.head and not self.tail:
            return None

        if self.head == self.tail:
            old_head = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return old_head.get_value()
        else:
            old_head = self.head
            self.head = self.head.get_next()
            self.size -= 1
            return old_head.get_value()

    def len(self):
        return self.size
