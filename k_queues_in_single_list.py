class Kqil:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.queue = [0] * n
        self.front = [-1] * k
        self.rear = [-1] * k
        self.next_available = 0
        self.next_index = list(range(1, n)) + [-1]

    def is_empty(self, qn):
        return self.front[qn] == -1

    def is_full(self):
        return self.next_available == -1

    def enqueue(self, value, qn):
        if self.is_full():
            print("Queue overflow")
            return
        new_index = self.next_available
        self.next_available = self.next_index[new_index]

        if self.is_empty(qn):
            self.front[qn] = new_index
        else:
            self.next_index[self.rear[qn]] = new_index

        self.next_index[new_index] = -1
        self.queue[new_index] = value
        self.rear[qn] = new_index

    def dequeue(self, qn):
        if self.is_empty(qn):
            print("Queue underflow")
            return

        front_index = self.front[qn]
        item = self.queue[front_index]

        self.front[qn] = self.next_index[front_index]
        self.next_index[front_index] = self.next_available
        self.next_available = front_index
        return item

q = Kqil(3, 10)
q.enqueue(3, 1)
q.enqueue(4, 1)
print(q.dequeue(1))
print(q.queue)