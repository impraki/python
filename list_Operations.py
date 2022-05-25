
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class List:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def show(self):
        temp = self.head
        while temp:
            print(f"{temp.data}->", end="")
            temp = temp.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


list1 = List()
list1.insert(1)
list1.insert(2)
list1.insert(3)
list1.insert(4)
list1.insert(5)
list1.append(6)
list1.show()
