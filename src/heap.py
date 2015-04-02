import heapq

class MinHeap:
    def __init__(self, x=[]):
        self.heap = [e for e in x]
        heapq.heapify(self.heap)
    def push(self, item):
        heapq.heappush(self.heap, item)
    def pop(self):
        return heapq.heappop(self.heap)
    def pushpop(self, item):
        return heapq.heappushpop(self.heap, item)
    def reset(self):
        heapq.heapify(self.heap)
    def replace(self, NewItem, pos):
        self.heap[pos] = NewItem
        heapq.heapify(self.heap)
    def root(self):
        return self.heap[0]

class MaxHeap(MinHeap):
    def __init__(self, x=[] ):
        self.heap = [-e for e in x]
        heapq.heapify(self.heap)
    def push(self, item):
        heapq.heappush(self.heap, -item)
    def pop(self):
        return -heapq.heappop(self.heap)
    def pushpop(self, item):
        return -heapq.heappushpop(self.heap, -item)
    def replace(self, NewItem, pos):
        self.heap[pos] = -NewItem
        heapq.heapify(self.heap)
    def root(self):
        if len(self.heap) ==0: return
        return -self.heap[0]


class MinMaxBalancedHeap:
    def __init__( self ):
        self.minHeap = MinHeap()
        self.maxHeap = MaxHeap()
        self.lengthminheap = 0
        self.lengthmaxheap = 0
    
    def push( self, item ):
        if item > self.maxHeap.root():
            if self.lengthmaxheap == self.lengthminheap:
                self.minHeap.push( item )
                self.lengthminheap += 1
            else:
                self.maxHeap.push( self.minHeap.pushpop( item ) )
                self.lengthmaxheap += 1
        else:
            if self.lengthmaxheap == self.lengthminheap:
                self.minHeap.push( self.maxHeap.pushpop( item ) )
                self.lengthminheap += 1
            else:
                self.maxHeap.push( item )
                self.lengthmaxheap += 1

    def replace( self, pos, item ):
        if pos < self.lengthmaxheap:
            self.maxHeap.replace( item, pos )
        else:
            self.minHeap.replace( item, pos - self.lengthmaxheap )
        if self.maxHeap.root() > self.minHeap.root():
            self.maxHeap.push( self.minHeap.pushpop( self.maxHeap.pop() ) )

    def getMedian( self ):
        if self.lengthminheap == self.lengthmaxheap:
            return .5*(self.minHeap.root() + self.maxHeap.root())
        elif self.lengthminheap > self.lengthmaxheap:
            return self.minHeap.root()
        else:
            return self.maxHeap.root()
    
    def getSize( self ):
        return self.lengthminheap + self.lengthmaxheap

    def printSize( self ):
        print "minHeapSize = ", self.lengthminheap, \
              "maxHeapSize = ", self.lengthmaxheap
    
    def printHeap( self ):
        print self.minHeap.heap
        print self.maxHeap.heap

if __name__ == "__main__":
    # Simple test
    data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print 'original data are', data
    minheap = heap.MinHeap(data)
    maxheap = heap.MaxHeap(data)
    print 'min heap is:', minheap.heap
    print 'max heap is:', maxheap.heap
    minheap.replace(-1, 9)
    print 'replace 9 with -1, now min heap root is:', minheap.root()
    maxheap.replace(-1, 9)
    print 'replace 9 with -1, now max heap root is:', maxheap.root()
