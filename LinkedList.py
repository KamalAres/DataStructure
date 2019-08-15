class Node:
    def __init__(self,x):
        self.data=x
        self.nxt=None
class LinkedList:
    def __init__(self):
        self.head=None
        
    def InsertAtBeg(self,newdata):
        newnode=Node(newdata)
        newnode.nxt=self.head
        self.head=newnode

    def InsertAtMid(self,newdata,mid):
        newnode=Node(newdata)
        #temp=Node()
        temp=self.head
        count=1
        while temp:
            if count==mid:
                newnode.nxt=temp.nxt
                temp.nxt=newnode
        temp=temp.nxt
        count=count+1
                
            
    def InsertAtEnd(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        last=self.head
        while last.nxt:
            last=last.nxt
        last.nxt=newnode
        
    def DeleteAtBeg(self):
        temp=self.head
        self.head=self.head.nxt
        temp=None
    #def DeleteAtMid():

    def DeleteAtEnd(self):
        temp=self.head
        while temp:
            if temp.nxt is None:
                temp=None
            
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,"==>",end='')
            temp=temp.nxt
        print("None")
            

obj=LinkedList()
ch=0
while(ch!=4):
    
    print("\nImplementation of the linked list\n1.Insert at beginning \n2.Insert at middle\n3.Insert at end\n4.Delete at beginning \n5.Delete at middle\n6.Delete at end\n7.print List \n8.Exit\n")
    ch=int(input("Enter your choice"))
    if ch==1:
        a=input("Enter the data to input:")
        obj.InsertAtBeg(a)
        obj.printList()
    elif ch==2:
        a=input("Enter the data to input at middle:")
        b=int(input("Enter the middle node where to insert data:"))
        obj.InsertAtMid(a,b)
        obj.printList()
    elif ch==3:
        a=input("Enter the data to input at end:")
        obj.InsertAtEnd(a)
        obj.printList()
    elif ch==4:
        obj.DeleteAtBeg()
        obj.printList()
    #elif ch==5:

    elif ch==6:
        obj.DeleteAtEnd()
        obj.printList()
        
    elif ch==7:
        obj.printList()
    else:
        print("Invalid operation")
