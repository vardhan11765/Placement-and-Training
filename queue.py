'''class Queue:
    def __init__(self):
        self.que=[]
        self.front=None
        self.back=None
        self.length=0
    def is_empty(self):
        return self.length
    def enqueue(self,value):
        self.que.append(value)
        self.length+=1
        if self.length==1:
            self.front=0
            self.back=0
        else:
            self.front=0
            self.back=self.length-1
        return True
    def dequeue(self):
        if self.is_empty():
            x=self.que.pop(0)
            self.length-=1
            if self.length==1:
                self.front=0
                self.back=0
            elif self.length==0:
                self.front=None
                self.back=None
            else:
                self.front=0
                self.back=self.length-1
            return x
        else:
            return False
q=Queue()
q.enqueue(4)
#q.enqueue(55)
q.enqueue(200)
q.enqueue(23)
q.dequeue()
#q.dequeue()
#q.dequeue()
print(q.que)
print(q.front)
print(q.back)

'''
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Queue_1:
    def __init__(self):
        self.front=None
        self.back=None
    def is_empty(self):
        return self.front
    def enqueue(self,value):
        new_node=Node(value)
        if self.front is None:
            self.front=new_node
            self.back=new_node
        else:
            self.back.next=new_node
            self.back=new_node
        return True
    def dequeue(self):
        if not self.is_empty():
            print('Queue is empty')
            return
        if self.front==self.back:
            s=self.front.value
            self.front=None
            self.back=None
            return s
        x=self.front
        self.front=x.next
        x.next=None
        return x
    def display(self):
        if not self.is_empty():
            print('Queue is empty')
            return
        temp=self.front
        while temp is not None:
            print(temp.value)
            temp=temp.next
q1=Queue_1()
q1.enqueue(4)
q1.enqueue(5)
q1.enqueue(6)
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.display()
