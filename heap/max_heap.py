class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        item = self.storage[0]
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        self.storage.pop()
        self._sift_down(0)
        return item

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # loop until either the element reaches the top of the array
        # or we'lll break the loop when we realize the element's priority
        # is not larger than it's parents
        while index > 0:
            # the value at 'index' fetches the index of it's parent
            parent = (index-1)//2
            # check if element at 'index' has higher priority than the
            # element at the parent index
            if self.storage[index] > self.storage[parent]:
                # then we need to swap elements
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                # need to update the index
                index = parent
            else:
                # otherwise our element has reached a spot in the heap where
                # parent element has parent element
                break

    def _sift_down(self, index):
        left = (2*index)+1
        right = (2*index)+2
        if left < len(self.storage)-1 or right< len(self.storage)-1:
            if self.storage[left] < self.storage[right]:
                if self.storage[index] < self.storage[right]:
                    self.storage[index], self.storage[right] = self.storage[right], self.storage[index]
                    self._sift_down(right)
            else:
                if self.storage[index] < self.storage[left]:
                    self.storage[index], self.storage[left] = self.storage[left], self.storage[index]
                    self._sift_down(left)
