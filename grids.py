import arrays
class Grid(object):
    
    def __init__(self,rows,cols,fillValue=None):    
        self._arr=Array(rows)
        for i in range(rows):
            self._arr[i]=Array(cols,fillValue)
    def __getitem__(self,index):
        return self._arr[index]
    def __setitem__(self,index):
        
#对二维数组乃至更高维的数组，在底层上的输入都是一个index，
#这个值在运行中会改变，以此达到找到具体下标的功能


















#get和set都是对运算符【】的重载