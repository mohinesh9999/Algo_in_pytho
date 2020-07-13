class Node:
    def __init__(self, *args, **kwargs):
        self.value=args[0]
        self.next=None
def seggregate(head):
    even,odd=None,None
    evenh,oddh=None,None
    temp=head
    while(temp):
        if(temp.value%2==1):
            if(not odd):
                odd=Node(temp.value)
                oddh=odd
            else:
                odd.next=Node(temp.value)
                odd=odd.next
        else:
            if(not even):
                even=Node(temp.value)
                evenh=even
            else:
                even.next=Node(temp.value)
                even=even.next
        temp=temp.next
    odd.next=evenh
    if(even or odd):
        return head
    return oddh
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
x=seggregate(n0)
while(x):
    print(x.value,end=' ')
    x=x.next
print()