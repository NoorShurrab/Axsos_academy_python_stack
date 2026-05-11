class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")
        
    def peek(self):
        if len(self.queue) != 0:
            return self.queue[0]
        else:
            raise IndexError("Queue is empty")