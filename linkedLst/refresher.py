#convert linkedlist to integer

def list2num(head):
    st = ""
    while head:
        st += str(head.val)
        st = reversed(st)
        #or st[::-1]
        head = head.next
    return(int(st))

#convert integer to linkedlist
def stringToListNode(stringTotal):
    previousNode = None
    first = None
    for i in stringTotal:
        currentNode = ListNode(i)
        if first is None:
            first = currentNode
        if previousNode is not None:
            previousNode.next = currentNode
        previousNode = currentNode
    return first


