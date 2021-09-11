#class to create node
class Node:
    def __init__(self,value) :
        self.value=value
        self.next=None

#class for creating linked list
class LinkedList:
    def __init__(self,value) :
        new_node=Node(value)   #we create a new_node using our Node class
        self.head=new_node      #we assign the new_node as head as it is the only node
        self.tail=new_node       #we assign the new_node as tail as it is the only node
        self.length=1           #we assign the new_node as length as 1 as it is the only node

    #method to display our linkedlist
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

my_ll=LinkedList(210)
my_ll1=LinkedList(["priya","Biradar","Pratiksha","Patil"])
l1=LinkedList(34.56)
l1.display()
my_ll.display()          
my_ll1.display()          

       