class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_begin(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node        

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Test
#Queue
l = LinkedList()
l.insert_at_end(1)
l.insert_at_end(2)
l.insert_at_end(3)
l.display()

#Stack
ll = LinkedList()
ll.insert_at_begin(1)
ll.insert_at_begin(2)
ll.insert_at_begin(3)
ll.display()