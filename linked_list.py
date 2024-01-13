class Node():
    def __init__(self, data=None, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.last_node = None

    def print_linked_list(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f" {node.data} -> "
            node = node.next_node

        ll_string += "None"
        print(ll_string)