from LinkedList import LinkedList

class ImpConcepts(LinkedList):
    def __init__(self, list = None):
        super().__init__(list)
        
    # ~ Delete Nth Node From Last
    def deleteFromLast(self, n):
        if self.head.next == None:
            return None
        elif n == self.length:
            self.head = self.head.next
        
        indexToSearch = self.length - n
        prev = self.head
        i = 1
        while i < indexToSearch:
            prev = prev.next
            i += 1
        prev.next = prev.next.next
         

    # todo Reverse A Linked List
    # todo Check If The List Is A Palindrome


l = ImpConcepts([1,2,3,4,5])
l.deleteFromLast(5)
l.printList()