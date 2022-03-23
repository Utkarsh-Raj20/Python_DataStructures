from LinkedList import LinkedList


class ImpConcepts(LinkedList):
    def __init__(self, list=None):
        super().__init__(list)

    # ~ Delete Nth Node From Last
    def deleteFromLast(self, n):
        # checking for edge cases
        if self.head.next == None:
            return None
        elif n == self.length:
            self.head = self.head.next

        # finding the index to search in the list
        indexToSearch = self.length - n
        prev = self.head
        i = 1
        while i < indexToSearch:
            prev = prev.next
            i += 1
        prev.next = prev.next.next

    # todo Reverse A Linked List
    # ~ ITERATIVE
    def reverseIterate(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    # ~ RECURSIVE
    def reverseRecursive(self, head):
        if head == None or head.next == None:
            return head

        new_head = self.reverseRecursive(head.next)
        head.next.next = head
        head.next = None
        head = new_head

    # todo Check If The List Is A Palindrome


l = ImpConcepts([5, 7, 5, 9, 6, 5, 5, 2])
l.printList()
l.head = l.reverseRecursive(l.head)
l.printList()
