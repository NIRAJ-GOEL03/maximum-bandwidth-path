import sys

class Node:
    def __init__(self,name,value):
        self.name = name
        self.value = value


class Heap:  
    def __init__(self):
        self.heapList = [None]
        self.currentSize = 0
        self.index_dict = {}


    def heapifyUp(self,i):      
        while i // 2 > 0:
          if self.heapList[i].value > self.heapList[i // 2].value:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.index_dict[self.heapList[i].name] = i//2
             self.heapList[i] = tmp
             self.index_dict[tmp.name] = i
          i = i // 2

    def insertReal(self,k):
        self.heapList.append(k)
        self.index_dict[k.name] = self.currentSize+1
        self.currentSize = self.currentSize + 1
        self.heapifyUp(self.currentSize)

    def insert(self,name,value):
        self.insertReal(Node(name,value))

    def heapifyDown(self,i):       
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i].value < self.heapList[mc].value:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.index_dict[self.heapList[mc].name] = i
                self.heapList[mc] = tmp
                self.index_dict[tmp.name] = mc
            i = mc

    def maxChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2].value < self.heapList[i*2+1].value:
                return i * 2 + 1
            else:
                return i * 2

    def delMax(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.index_dict[self.heapList[self.currentSize].name] = 1
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.index_dict.pop(retval.name)
        self.heapifyDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.heapifyDown(i)
            i = i - 1
    
    def maximum(self):
        try:
            return self.heapList[1].name
        except:
            print "heap.py: Heap doesn't exist, Can't return maximum."

           
    def increaseKey(self,index, new_val):
        self.heapList[index].value =  new_val
        self.heapifyUp(index)

    def delete(self,name):
        ind = self.index_dict[name]
            
        self.increaseKey(ind,sys.maxint)
        self.delMax()
        return 0
        
    def update(self,name,value):
        ind = self.index_dict[name]
        self.increaseKey(ind,value)
        return 0

    def heapSort(self):
        pass
                    


def test():
    bh = Heap()
    n1 = Node(1,4)
    n2 = Node(2,43)
    n3 = Node(3,41)
    n4 = Node(4,214)
    n5 = Node(5,42)
    n6 = Node(6,24)
    n7 = Node(7,433)
    n9 = Node(9,433)
    n8 = Node(8,43)
    bh.insertReal(n1)
    bh.insertReal(n2)
    bh.insertReal(n3)
    bh.insertReal(n4)
    bh.insertReal(n5)
    bh.insertReal(n6)
    bh.insertReal(n7)
    bh.insertReal(n8)
    bh.insertReal(n9)
    bh.insert(9,9)
    print bh.maximum()
    print map(lambda i: i.value,bh.heapList[1:])
    bh.update(8,500)
    bh.update(6,506)
    bh.update(4,504)
    print map(lambda i: i.value,bh.heapList[1:])
    print bh.index_dict
    bh.update(2,503)
    bh.delete(2)
    bh.delete(6)
    print map(lambda i: i.value,bh.heapList[1:])
    print bh.index_dict
    bh.delete(4)
    print bh.maximum()
    print map(lambda i: (i.value,i.name),bh.heapList[1:])
    print bh.index_dict
    #bh.buildHeap([9,5,6,2,3])
    #print bh.heapList
    #print bh.maximum()
    #print(bh.delMin())
    #print bh.heapList
    #print(bh.delMin())
    #print bh.heapList
    #print(bh.delMin())
    #print bh.maximum()
    #print bh.heapList
    #print(bh.delMin())
    #print bh.heapList
    #print(bh.delMin())
    #print bh.maximum()
    #print bh.heapList
    #bh.insert(18)
    #bh.insert(8)
    #bh.insert(118)
    #print bh.heapList
    #bh.insert(7)
    #bh.insert(98)
    #print bh.heapList
    #print bh.maximum()

#test()

