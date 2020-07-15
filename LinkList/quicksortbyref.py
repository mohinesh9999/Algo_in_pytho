def qs(head,tail):
    if(head and tail and head !=tail):
        pivot1,pivot2=utility(head,tail)
        qs(head,pivot1)
        qs(pivot2,tail)
def printll(x):
    while(x):
        print(x.data,end=' ')
        x=x.next
    print()
def utility(head,tail):
    temp=head
    index=head
    prev,prevtemp,isf=None,None,True
    while(temp and temp!=tail):
        if(temp.data<tail.data):
            index.data,temp.data=temp.data,index.data
            prev=index
            index=index.next
        prevtemp=temp
        temp=temp.next
    index.data,tail.data=tail.data,index.data
    # printll(head)
    return [prev,index.next]
def quickSort(head):
    tail=head
    while(tail.next):
        tail=tail.next
    # print(tail.data)
    qs(head,tail)
    return head
class Node:
    def __init__(self, *args, **kwargs):
        self.data=args[0]
        self.next=None
n0=Node(17)
n1=Node(15)
n2=Node(8)
n3=Node(12)
n4=Node(10)
n5=Node(5)
n6=Node(4)

n0.next=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
printll(n0)
x=quickSort(n0)
while(x):
    print(x.data,end=' ')
    x=x.next
print()