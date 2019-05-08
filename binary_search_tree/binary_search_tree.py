class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        if value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

        if value <= self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    def contains(self, target):
        print(self.value, target)
        if target == self.value:
            return True
        elif target < self.value and self.left:
            self.left.contains(target)
        elif target > self.value and self.right:
            self.right.contains(target)
        else:
            return False

    def get_max(self):
        pass
        # current_max = self.value
        # current_node = self
        # while current_node.right != None:
        #     if current_max < current_node.value:
        #         current_max = current_node.value
        #         current_node.value = self.right

        # return current_max

    def for_each(self, cb):
        pass
