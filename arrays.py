class Array(object):
    def __init__(self,capacity,fillValue=None):
        self._item=list()
        for _ in range(capacity):
            self._item.append(fillValue)
            
    def __len__(self):
        return len(self._item)
    
    def __str__(self):
        return str(self._item)
    
    def __getitem__(self,index):
        if(index>=len(self._item)):
            raise IndexError("index have to range[0,"+str(len(self._item)-1)+"]")
        return self._item[index]
    
    
    def __setitem__(self,index,value):
        if(index>=len(self._item)):
            for _ in range(len(self._item),index+1):
                self._item.append(fillValue)
        self._item[index]=value
        
    def __iter__(self):#实现迭代功能要重载的类
        cursor=0
        while cursor<len(self):
            yield self._item[cursor]
            cursor+=1
            
    
if __name__=="__main__":
    arr=Array(3,0)
    len(arr)
    print(arr)
    for data in arr:
        print(data)
        