class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    # ~ initializing the stack
    # ~ using dummy node which help in

    def __init__(self) -> None:
        self.head = Node("head")
        self.size = 0
