def insert(root,key):
    temp=root
    for i in key:
        if(temp.children[charToIndex(i)]!=None):
            temp=temp.children[charToIndex(i)]
        else:
            temp.children[charToIndex(i)]=TrieNode()
            temp=temp.children[charToIndex(i)]
    temp.isEndOfWord=True
            


def search(root, key):
    flag=True
    temp=root
    for i in key:
        if(temp.children[charToIndex(i)]!=None):
            temp=temp.children[charToIndex(i)]
        else:
            flag=False
    return flag and temp.isEndOfWord