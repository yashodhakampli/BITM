class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            new_node.prev = last_node

    def add_mid(self, data, position):
        if position <= 0:
            self.add_first(data)
        else:
            new_node = Node(data)
            current_node = self.head
            for _ in range(position - 1):
                if current_node is None:
                    print("Position out of range")
                    return
                current_node = current_node.next
            if current_node is None:
                print("Position out of range")
                return
            new_node.next = current_node.next
            if current_node.next:
                current_node.next.prev = new_node
            current_node.next = new_node
            new_node.prev = current_node

    def remove_first(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def remove_last(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def remove_mid(self, position):
        if self.head is None:
            print("List is empty")
            return
        if position <= 0:
            self.remove_first()
        else:
            current_node = self.head
            for _ in range(position):
                if current_node is None:
                    print("Position out of range")
                    return
                current_node = current_node.next
            if current_node is None:
                print("Position out of range")
                return
            if current_node.next:
                current_node.next.prev = current_node.prev
            current_node.prev.next = current_node.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")


# Main program
linked_list = DoublyLinkedList()

while True:
    print("\n1. Add node at first")
    print("2. Add node at last")
    print("3. Add node at middle")
    print("4. Remove node at first")
    print("5. Remove node at last")
    print("6. Remove node at middle")
    print("7. Display the list")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        data = input("Enter data to add at first: ")
        linked_list.add_first(data)
    elif choice == '2':
        data = input("Enter data to add at last: ")
        linked_list.add_last(data)
    elif choice == '3':
        data = input("Enter data to add: ")
        position = int(input("Enter position to add (0 for first): "))
        linked_list.add_mid(data, position)
    elif choice == '4':
        linked_list.remove_first()
    elif choice == '5':
        linked_list.remove_last()
    elif choice == '6':
        position = int(input("Enter position to remove (0 for first): "))
        linked_list.remove_mid(position)
    elif choice == '7':
        linked_list.display()
    elif choice == '8':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")