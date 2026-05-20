# This code implements a Singly Linked List data structure in Python, featuring basic node creation.
# It includes methods to insert elements at both the front and back of the list, and to print the chain sequentially.
class SLNode:
    def __init__(self, val):
        self.value = val   
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    
    def add_to_front(self, val):
        new_node = SLNode(val)       
        current_head = self.head     
        new_node.next = current_head 
        self.head = new_node        
        return self
    
    def print_values(self):
        runner = self.head
        while runner != None:
            if runner.next != None:
                print(runner.value, end="-")
            else:
                print(runner.value)

            runner = runner.next
        return self

    def add_to_back(self, val):
        if self.head == None:
            return self.add_to_front(val) 

        new_node = SLNode(val)   
        runner = self.head   

        while (runner.next != None):
            runner = runner.next
            
        runner.next = new_node
        return self
    
my_list = SList()
#my_list.add_to_front("A").add_to_front("B").add_to_front("C").add_to_front("D")
my_list.add_to_back("A").add_to_back("B").add_to_back("C").add_to_back("D")
my_list.print_values()