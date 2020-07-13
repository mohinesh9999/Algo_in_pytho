class Node:
    def __init__(self, *args, **kwargs):
        self.value=args[0]
        self.next=None

def intersectionPoint(head1,head2):
    s=set()
    temp=head1
    while(temp):
        s.add(temp)
        temp=temp.next
    temp=head2
    while(temp and temp not in s):
        temp=temp.next
    return temp



n0=Node(1)
n1=Node(3)
n2=Node(6)
n3=Node(2)
n4=Node(4)
n5=Node(5)

n0.next=n1
n1.next=n2
n3.next=n3
n3.next=n4
n4.next=n5
#implementing LRU cache by doubly link list of size 6
x=merge(n0,n3)
printll(x)








n0=Node(17)
n1=Node(15)
n2=Node(8)
n3=Node(12)
n4=Node(10)
n5=Node(5)
n6=Node(4)
ne=Node(1)
n0.next=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
ne.next=n3
print(intersectionPoint(n0,ne).value)

'''count len of both link list
    put pointer of bigger linklist into c2-c1 pos
    and now run pointer ahaed first common is intersection point


'''