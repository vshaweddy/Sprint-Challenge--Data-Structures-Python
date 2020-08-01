class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.cur = 0

    def append(self, item):
        if self.cur < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.cur % self.capacity] = item
        self.cur += 1

    def get(self):
        return self.storage