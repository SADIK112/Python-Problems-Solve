class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)

    def length_of_list(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def remove_at(self, index):
        if index < 0 or index > self.length_of_list():
            raise Exception("Index out of range")
            return

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        curr = self.head
        while curr:
            if count == index - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.length_of_list():
            raise Exception("Index out of range")
            return

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        curr = self.head
        while curr:
            if count == index - 1:
                node = Node(data, curr.next)
                curr.next = node
                break
            curr = curr.next
            count += 1
    
    def print(self):
        if self.head is None:
            print("List is empty...")
            return
            
        curr = self.head
        currentList = ""

        while curr:
            currentList += str(curr.data) + "->"
            curr = curr.next
        print(currentList)
