class Node:
    def __init__(self, *args, **kwargs):
        self.value=args[0]
        self.next=None

class singlyLinkList:
    def __init__(self, *args, **kwargs):
        self.head=None
        self.tail=None
        self.len=0
    def addNode(self,value):
        if(not self.head):
            self.head=Node(value)
            self.tail=self.head
        else:
            node=Node(value)
            self.tail.next=node
            self.tail=self.tail.next
        self.len+=1
    def addll(self,ll):
        self.head=ll
    def print(self):
        temp=self.head
        while(temp):
            print(temp.value,end=' ')
            temp=temp.next
        print()
    #Reverse in k groups
    def reverseInGroups(self,k):
        if(self.len<=1):
            return
        else:
            curr,prev,temp,fp=self.head,None,None,True
            while(curr):
                temp_head=curr
                temp_prev=prev
                count=0
                while(count<k and curr):
                    count+=1
                    temp=curr.next
                    curr.next=prev
                    prev=curr
                    curr=temp
                if(fp):
                    self.head=prev
                    fp=False
                else:
                    temp_prev.next=prev
                temp_head.next=curr
                prev=temp_head  
    #floyd cycle detection 
    def detectLoop(self):
        temp1,temp2=self.head,self.head
        flag=False
        prev=None
        while(temp1 and temp2):
            prev=temp1
            temp1=temp1.next
            temp2=temp2.next.next if(temp2.next and temp2.next.next) else None
            if(not temp2):
                break
            elif(temp1 is temp2):
                flag=True
                break
        if(flag):
            print('loop')
            temp1=self.head
            while(temp1.next!=temp2.next):
                temp1=temp1.next
                temp2=temp2.next
            temp2.next=None
            self.print()
        else:
            print('straight')
            return
    #delete node with refrence without using head refrence
    def deleteNode(self,node):
        prev=None
        while(node.next):
            prev=node
            node.value=node.next.value
            node=node.next
        prev.next=None


























#Test class
#Create a link list of length 6
# linkList=singlyLinkList()
# for i in range(6):
#     linkList.addNode(int(input()))
# linkList.print()
# linkList.reverseInGroups(4) #change k as per groups
# linkList.print()
# linkList.detectLoop()
linkListloop=singlyLinkList()
n1=Node(6)
n2=Node(5)
n3=Node(5)
n1.next=n2
n2.next=n3
n3.next=None
linkListloop.addll(n1)
linkListloop.print()
linkListloop.deleteNode(n2)#node cant be last 
linkListloop.print()
# linkListloop.detectLoop()
#didnt detect circcular link list
# n3=Node(5)
# s=set()
# s.add(n3)
# n4=n3
# print(n4 in s,n3==n4,n3 is n4)
# n5=Node(5)
# print(n5 in s,n3==n5,n3 is n5)