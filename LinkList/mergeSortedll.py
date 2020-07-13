class Node:
    def __init__(self, *args, **kwargs):
        self.value=args[0]
        self.next=None
def printll(x):
    while(x):
        print(x.value,end=' ')
        x=x.next
    print()
def merge(h1,h2):
    a,b=h1,h2
    head,tail=None,None
    while(a and b):
        if(a.value<b.value):
            if(not head):
                head=a
                tail=a
                a=a.next
            else:
                tail.next=a
                tail=tail.next
                a=a.next
        else:
            if(not head):
                head=b
                tail=b
                b=b.next
            else:
                tail.next=b
                tail=tail.next
                b=b.next
        if(a):
            tail.next=a
        if(b):
            tail.next=b
    return head
n0=Node(1)
n1=Node(3)
n2=Node(6)
n3=Node(2)
n4=Node(4)
n5=Node(5)

n0.next=n1
n1.next=n2
n3.next=n4
n4.next=n5

x=merge(n0,n3)
printll(x)