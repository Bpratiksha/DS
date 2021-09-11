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
        while temp is not None:         #if head is not none thn value will assign nd dispaly
            print(temp.value)
            temp=temp.next
    
    #append function to insert new node at the end
    def append(self,value):
        new_node=Node(value)             #so we create a node with value
        if self.head is None:           #we check if our linkedlist is empty
            self.head=new_node          #if empty we put our node as head and tail both
            self.tail=new_node
        else:
            self.tail.next=new_node     #we point the last node of our list to new node
            self.tail=new_node          #make our newly added node as the tail
        self.length+=1                  #finally increase the length of our list
        return True

e1=LinkedList(13)
e1.append(23)
e1.append(33)
e1.append(43)
e1.append(53)
e1.display()
