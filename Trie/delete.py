def delkey(root,key,i):
    if(not root):
        return root
    if i==len(key):
        root.isend=False
        if(isEmpty(root)):
            root=None
            return root
        return root
    index=ord(key[i])-ord('a')
    root.child[index]=delkey(root, key,i+1)
    if(isEmpty(root) and root.isend==False):
        root=None
        return root
    return root
def isend(root):
    for i in range(26):
        if(not root.child[i]):
            return False
    return True