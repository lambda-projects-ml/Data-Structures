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
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)
        else:
            return False

    def get_max(self):
        # pass
        current_max = self.value

        while self.right != None:
            if current_max < self.value:
                return self.right.get_max()

            return current_max

    def for_each(self, cb):
        pass
