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
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def dequeue(self):
        dequeued_node = self.head
        if not self.head and not self.tail:
            return None

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()

        return dequeued_node.value

    def len(self):
        count = 0
        current_node = self.head
        while current_node != None:
            count += 1
            current_node = current_node.get_next()
        return count
