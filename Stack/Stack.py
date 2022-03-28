# ~ Implementation of Stack using linked list
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedStack:
    # ~ initializing the stack
    # ~ using dummy node which help in handling edge cases

    def __init__(self, lis=None) -> None:
        self.values = lis
        self.size = 0
        self.head = self.createStack()

    def createStack(self):
        # * if the list is not passed

        if self.values is None:
            return Node("Stack")

        # * if the list is passed 
        # * creating the head node
        self.head = Node("Stack")

        # * adding the values using push method one by one
        for x in self.values:
            self.push(x)
        return self.head

    def __str__(self):
        # * represents how the list will print
        if self.head.next is None:
            return "Empty Stack"
        cur = self.head.next
        out = "Stack: "
        while cur:
            out += str(cur.data) + " -> "
            cur = cur.next
        return out[:-3]

    def push(self, data):
        # * creating the node of passed data
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

        # * increasing the size of the stack
        self.size += 1

    def pop(self):
        # * checking for an empty stack
        if self.isEmpty():
            print("Popping from an Empty Stack")

        # * removing the topmost element for the stack
        top = self.head.next
        self.head.next = top.next

        # * returning the data of topmost element
        return top.data

    def peak(self):
        # * checking for an empty stack
        if self.isEmpty():
            print("Peeking from an Empty Stack")
            return

        # * returning the topmost data without removing the element
        return self.head.next.data

    def isEmpty(self):
        # * checks if the stack is empty or not
        return self.size == 0

    def getSize(self):
        # * returns the size of the stack
        return self.size


# ~ Implementation of Stack using array
class ArrayStack:
    def __init__(self, lis=None) -> None:
        self.values = lis
        self.stack = []
        self.top = None
        self.size = 0

    def __str__(self):
        if self.size == 0:
            return 'Empty Stack'
        out = ""
        for x in self.stack:
            out += str(x) + " -> "
        return out[:-3]

    def push(self, data):
        if self.size == 0:
            self.stack.append(data)
            self.size += 1
            self.top = self.stack[0]
        else:
            self.stack.insert(0, data)
            self.top = self.stack[0]
            self.size += 1

    def peak(self):
        return self.top

    def pop(self):
        self.stack.pop(0)
        self.top = self.stack[0]
        self.size -=1

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

