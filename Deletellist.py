
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
class LinkedList:   
    def __init__(self): 
        self.head = None 
    def insert(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head 
        self.head = new_node 
    def deleteNode(self, key): 
        temp = self.head 
        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next 
                temp = None 
                return
        while(temp is not None): 
            if temp.data == key: 
                break 
            prev = temp 
            temp = temp.next
        if(temp == None): 
            return 
        prev.next = temp.next 
        temp = None 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data), 
            temp = temp.next   
llist = LinkedList() 
llist.insert(1) 
llist.insert(2) 
llist.insert(3) 
llist.insert(4)   
print "Created Linked List: " 
llist.printList() 
llist.deleteNode(2)  
print "\nLinked List after Deletion of 2:" 
llist.printList() 




  
