class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        
    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == 0 or (-1*self.maxHeap[0]) >= num:
            heappush(self.maxHeap,-num)
        else:
            heappush(self.minHeap,num)
        self.balance()
    
    def balance(self):
        if len(self.maxHeap) - len(self.minHeap) > 1:
            heappush(self.minHeap,-1* heappop(self.maxHeap))
        elif len(self.minHeap) - len(self.maxHeap) > 1:
            heappush(self.maxHeap,-1*heappop(self.minHeap))
         
    def findMedian(self) -> float:
        #print('median')
        #print(self.maxHeap,self.minHeap)
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return ((-1 *self.maxHeap[0]) + self.minHeap[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()