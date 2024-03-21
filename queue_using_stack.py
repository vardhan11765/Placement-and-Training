'''Queue using single Stack'''


class Queueusingstack:
    def __init__(self):
        self.stack=[]
    def enqueue(self,value):
        self.stack.append(value)
    def dequeue(self):
        if not self.stack:
            return 'Queue is empty'
        elif len(self.stack)==1:
            return self.stack.pop()
        else:
            front=self.stack.pop()
            d_i=self.dequeue()
            self.stack.append(front)
            return d_i
    def peek(self):
        if not self.stack:
            return 'Queue is empty'
        return self.stack[0]
    def is_empty(self):
        return len(self.stack)
    
q=Queueusingstack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.dequeue()
print(q.stack)
