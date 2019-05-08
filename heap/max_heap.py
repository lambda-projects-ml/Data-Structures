class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

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
        pass
