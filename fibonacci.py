class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.insert(0,str(node.data))
            node = node.next
        return " , ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def add_first(self,node):
        node.next = self.head
        self.head = node
    
    def add_last(self,node):
        if not self.head:
            self.head = node
            return
        for currrent_node in self:
            pass
        currrent_node.next=node

def compute(n):
    fiboSeries = [0,1]
    node = Node(0)
    llist = LinkedList()
    llist.add_first(node)

    node = Node(1)
    llist.add_last(node)
     
    while n-2 > 0 :
        n-=1
        res = fiboSeries[len(fiboSeries)-1]+fiboSeries[len(fiboSeries)-2]
        fiboSeries.append(res)
        node = Node(fiboSeries[len(fiboSeries)-1])
        llist.add_last(node)
    return llist

if __name__ == "__main__":
    n = 100
    llist = compute(n)
    print(llist)
   
    

 
    
    
   

    