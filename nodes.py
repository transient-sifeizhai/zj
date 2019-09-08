class Nodes(object):
    def __init__(self,item,next=None):
        self._item=item
        self.next=next
        
        
if __name__=="__main__":
    """   
    node4=Nodes(4)
    node3=Nodes(3,node4)
    node2=Nodes(2,node3)
    node1=Nodes(1,node2)
    head=node1
    """

    for i in range(1,11):
        head=Nodes(i,head)
        
    """    
    while head!=None:
        print(head._item)
        head=head.next
    #该种写法没有实用意义，因为这样遍历出来会丢失头，也就是会丢失整个链表
    """
    
    #正确写法
    temp=head
    while temp!=None:
        print(temp._item)
        temp=temp.next
        
