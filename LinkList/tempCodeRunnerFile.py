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