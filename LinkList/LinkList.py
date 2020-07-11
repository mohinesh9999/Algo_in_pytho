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
                








#Create a link list of length 6
linkList=singlyLinkList()
for i in range(6):
    linkList.addNode(int(input()))
linkList.print()
linkList.reverseInGroups(4) #change k as per groups
linkList.print()
    