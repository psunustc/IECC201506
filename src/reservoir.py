import heap, random

class reservoir:
    def __init__( self, N = 20000 ):
        self.heap = heap.MinMaxBalancedHeap()
        self.maxsize = N
        self.runningMax = 0
        
    def push( self, value ):
        self.runningMax += 1
        if self.heap.getSize() < self.maxsize:
            self.heap.push( value )
        else:
            pos = int( random.random() * self.runningMax )
            if pos < self.maxsize:
                self.heap.replace( pos, value )

    def getMedian( self):
        return self.heap.getMedian()
    
    def getRunningMedian( self, value ):
        self.push( value )
        return self.getMedian()

    def printHeapSize( self ):
        self.heap.printSize()

if __name__ == "__main__":
    n = 20000
    nn = 2000
    res = reservoir( n )
    for i in xrange( 10*n ):
        res.push(i)
        if ( i + 1 ) % nn == 0: 
            res.printHeapSize()
            print i*.5, res.getMedian()
