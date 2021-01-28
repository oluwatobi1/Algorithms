# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def condense(head):
    # Write your code here
    store = set()
    out = []
    # out = SinglyLinkedListNode(None)
    
    while head!=None:        
        if head.data not in store:
            out.append(head.data)
        store.add(head.data)
        head = head.next    
    out_linked = None
    
    for i in out[::-1]:
        temp = SinglyLinkedListNode(i)
        temp.next= out_linked
        out_linked=temp
    return out_linked






# if __name__ == '__main__':