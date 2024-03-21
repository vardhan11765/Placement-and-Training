class Queueusingstacks:
    def __init__(self):
        self.stack_enqueue=[]
        self.stack_dequeue=[]
    def enqueue(self,value):
        self.stack_enqueue.append(value)
    def dequeue(self):
        if not self.stack_dequeue:
            if not self.stack_enqueue:
                return 'Queue is empty'
        else:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue.pop()
    def peek(self):
        if not self.stack_dequeue:
            if not self.stack_enqueue:
                return 'Queue is empty'
        else:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue[-1]
    def is_empty(self):
        return not self.stack_enqueue and not self.stack_dequeue
    
q=Queueusingstacks()
q.enqueue(4)
q.enqueue(3)
q.enqueue(2)
print(q.dequeue())