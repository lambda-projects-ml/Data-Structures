"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return self.head.value
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
            self.length += 1
            return self.head.value

    def remove_from_head(self):
        if self.head == None:
            self.length = 0
        elif self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return value
        else:
            new_head = self.head.next
            value = self.head.value
            self.head.delete()
            self.head = new_head
            self.length -= 1
            return value

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return self.head.value
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            self.length += 1
            return self.tail.value

    def remove_from_tail(self):
        if self.head == None:
            self.length = 0
        elif self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return value
        else:
            new_tail = self.tail.prev
            value = self.tail.value
            self.tail.delete()
            self.tail = new_tail
            self.length -= 1
            return value

    def move_to_front(self, node):
        self.add_to_head(node.value)
        self.delete(node)

    def move_to_end(self, node):
        self.add_to_tail(node.value)
        self.delete(node)

    def delete(self, node):
        if self.head == self.tail:
            self.remove_from_head()
        elif node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1

    def get_max(self):
        current_node = self.head
        maxValue = self.head.value
        while current_node.next != None:
            current_node = current_node.next
            if current_node.value > maxValue:
                maxValue = current_node.value

        return maxValue
