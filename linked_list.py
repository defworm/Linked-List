class Node:
  def __init__(self, data, reference=None):
    self.data = data
    self.reference = reference

class LinkedList:
    def __init__(self, head=None):
        self.head=head

    def print_linked_list (self):
        if self.head == None:
            print ("Linked list is empty")
        else:
            c_node = self.head
            while c_node is not None:
                print (f"Data: {c_node.data}")
                c_node = c_node.reference

    def add_to_start(self, data):
        n_node = Node(data)
        n_node.reference = self.head
        self.head = n_node

    def add_item(self, data):
        n_node = Node(data)
        c_node = self.head
        while c_node is not None:
            next_node = c_node.reference
            if next_node == None:
                c_node.reference = n_node
                break
            else:
                c_node = next_node



if __name__ == "__main__":
    # node1 = Node (5)
    # node2 = Node (11)
    # node1.reference = node2
    # print (node1.data, node1.reference)
    l_list1 = LinkedList()
    l_list1.add_to_start(42)
    l_list1.print_linked_list()
    l_list1.add_to_start(15)
    l_list1.print_linked_list()
    l_list1.add_item(88)
    l_list1.print_linked_list()