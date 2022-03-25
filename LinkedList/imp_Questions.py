from LinkedList import LinkedList


class ImpConcepts(LinkedList):
    def __init__(self, list=None):
        super().__init__(list)

    # ~ Delete Nth Node From Last
    def deleteFromLast(self, n):
        # checking for edge cases
        if self.head.next == None:
            return None
        elif n == self.size():
            self.head = self.head.next

        # finding the index to search in the list
        indexToSearch = self.length - n
        prev = self.head
        i = 1
        while i < indexToSearch:
            prev = prev.next
            i += 1
        prev.next = prev.next.next
    

    # ------------------------------------------------------------------------#


    # ~ Reverse A Linked List

    # * ITERATIVE
    def reverseIterate(self, head=None):
        prev = None

        # checking if head is given or not
        if head is None:
            curr = self.head
        else:
            curr = head

        # main reverse loop
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # checking if head is given or not
        if head is None:
            self.head = prev
        else:
            head = prev
            return head

    # * RECURSIVE
    def reverseRecursive(self, head):

        # edge cases
        if head == None or head.next == None:
            return head

        # recursice calls
        new_head = self.reverseRecursive(head.next)
        head.next.next = head
        head.next = None
        return new_head


    # ------------------------------------------------------------------------#


    # ~ Check If The List Is A Palindrome

    def isPalindrome(self):
        firstHalfEnd = self.middle()
        secondHalf = self.reverseIterate(firstHalfEnd.next)
        firstHalf = self.head
        while secondHalf:
            if secondHalf.data != firstHalf.data:
                return False
            else:
                secondHalf = secondHalf.next
                firstHalf = firstHalf.next
        return True

    # * finding the middle of the linked list
    def middle(self):
        turtle = self.head
        hare = self.head
        while hare:
            if hare.next is None or hare.next.next is None:
                return turtle
            turtle = turtle.next
            hare = hare.next.next


    
l = ImpConcepts([1, 2, 2, 1])
print("Original List:", end=" ")
l.printList()
# l.reverseIterate()  #? Iterative
l.head = l.reverseRecursive(l.head) #? Recursive
print("Reversed List:", end=" ")
l.printList()

if l.isPalindrome:
    print("So this is a Palindrome Linked List")
else:
    print("So this is not a Palindrome")
