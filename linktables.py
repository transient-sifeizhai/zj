class LinkTables(object):
    def __init__(self,item,next=None):
        self._item=item
        self.next=next
        
    def __str__(self,head):
        self.temp=head
        while temp!=None:
            print(temp.item)
            temp=temp.next
    
#写链表的str方法
if __name__=="__main__":
    
        
    