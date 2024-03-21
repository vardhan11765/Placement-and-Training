class minstack:
    def __init__(self):
        self.l=[]
        self.top=-1
    def push(self,value):
        self.l.append(value)
        self.top+=1
        return True
    def pop(self):
        if self.top==-1:
            return False
        x=self.l.pop()
        self.top-=1
        return x
    def tope(self):
        return self.top
    def minele(self):
        return min(self.l)
    
s=minstack()
s.push(2)
s.push(6)
s.push(7)
s.push(4)
print(s.l)
s.pop()
print(s.l)
print(s.minele())
