class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicate(head: ListNode): 

    if head == None: 
        return head 
    
    prev = head 
    
    while prev.next != None: 
        if prev.next.val == prev.val: 
            prev.next = prev.next.next 
        else: 
            prev = prev.next 
    return head 

    