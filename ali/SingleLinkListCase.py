"""
如何实现一个高效的单向链表逆序输出？
出题人：阿里巴巴出题专家：昀龙／阿里云弹性人工智能负责人
参考答案：下面是其中一种写法，也可以有不同的写法，比如递归等。供参考
"""

"""
结构：
链表SingleLinkedlist中的每个元素都是一个对象，每个对象有一个关键字key和一个指针：next
解题思路:
在C的时候我们使用三个指针遍历单链表，逐个链接点进行反转
"""



class Node:#定义节点
   def __init__(self, initdata):
        self.__data = initdata
        self.__next = None
   def getData(self):
        return self.__data
   def getNext(self):
        return self.__next
   def setData(self, newdata):
        self.__data = newdata
   def setNext(self, newnext):
        self.__next = newnext
class SingleLinkedlist:
    def __init__(self):
        self.head = Node(None) # 头节点赋值None
        self.head.setNext(self.head)
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head.getNext())
        self.head.setNext(temp)
    def reverse(self):
        header =self.head
        if header == None or header.getNext().getData() == None:
            pass
        p1 = header       #p1,p2,p3就相当于C语言里的三个指针
        p2 = p1.getNext()
        while(p2.getData()!=None):
            p3 = p2.getNext()
            p2.setNext(p1)
            p1 = p2
            p2 = p3
        header.setNext(None)
        header = p1
        self.head.setData(None)
        self.head.setNext(p1)
    def print_list(self):
        l = []
        p =self.head
        if p.getData()!= None:
            l.append(p.getData())
        while (p.getNext().getData()!= None):
            p = p.getNext()
            l.append(p.getData())
        print(l)
if __name__ == '__main__':
    s = SingleLinkedlist()
    s.add(10)
    s.add(9)
    s.add(8)
    s.add(7)
    s.add(6)
    s.add(5)
    s.print_list()
    p =s.head
    s.reverse()
    print("After reverse...")
    s.print_list()