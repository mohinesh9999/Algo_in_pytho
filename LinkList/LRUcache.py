class Node:
    def __init__(self, *args, **kwargs):
        self.value=args[0]
        self.next=None
        self.prev=None
def printll(x):
    while(x):
        print(x.value,end=' ')
        x=x.next


tail=None
def cache(x1,y,d):
    global tail
    # d=dict()
    x=x1
    if(y in d):
        print('hit')
        y=d[y]
        if(y != x1 and y!=tail):
            y.prev.next=y.next
            y.next.prev=y.prev
            y.next=x1
            x1.prev=y
            y.prev=None
            x1=y
        elif(y==tail):
            tail=y.prev
            y.prev.next=y.next
            y.next=x1
            x1.prev=y
            y.prev=None
            x1=y
        else:
            return x1
    else:
        print('miss')
        del d[tail.value]
        tail=tail.prev
        tail.next=None
        y1=Node(y)
        d[y]=y1
        y=y1
        y.next=x1
        x1.prev=y
        x1=y
    return x1
#implementing LRU cache by doubly link list of size 6
n0=Node(1)
n1=Node(3)
n2=Node(6)
n3=Node(2)
n4=Node(4)
n5=Node(5)

n0.next=n1
n1.prev=n0
n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3
n4.next=n5
n5.prev=n4
printll(n0)
x=n0
d=dict()
while(x):
    d[x.value]=x
    x=x.next
tail=n5
for i in range(10):
    n0=cache(n0,int(input()),d)
    printll(n0)
    print()