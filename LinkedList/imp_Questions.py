from LinkedList import LinkedList


class ImpConcepts(LinkedList):
    def __init__(self, lis=None):
        super().__init__(lis)

    # ~ Delete Nth Node From Last
    def deleteFromLast(self, n):
        # checking for edge cases
        if self.head.next is None:
            return None
        elif n == self.size():
            self.head = self.head.next

        # finding the index to search in the list
        index_to_search = self.length - n
        prev = self.head
        i = 1
        while i < index_to_search:
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
        if head is None or head.next is None:
            return head

        # recursive calls
        new_head = self.reverseRecursive(head.next)
        head.next.next = head
        head.next = None
        return new_head

    # ------------------------------------------------------------------------#

    # ~ Check If The List Is A Palindrome

    def isPalindrome(self):
        first_half_end = self.middle()
        second_half = self.reverseIterate(first_half_end.next)
        first_half = self.head
        while second_half:
            if second_half.data != first_half.data:
                return False
            else:
                second_half = second_half.next
                first_half = first_half.next
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


n = int(input("size of list: "))
print("Enter the items of list: ", end="")
test = list(map(str, input().split()))

l = ImpConcepts(test)
print("Original List:", end=" ")
l.printList()
# l.reverseIterate()  #? Iterative
l.head = l.reverseRecursive(l.head)  # ? Recursive
print("Reversed List:", end=" ")
l.printList()

if l.isPalindrome:
    print("So this is a Palindrome Linked List")
else:
    print("So this is not a Palindrome")
