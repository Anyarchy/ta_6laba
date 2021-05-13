from itertools import islice

class MaxHeap:
   
    def __init__(self):
        
        self.heap = []
        
    def Size(self):

       return len(self.heap)
    
    def Max(self):
 
        max = 0
        for x in range(self.Size()):
          if self.heap[x] > max:
               max = self.heap[x] 
        return max
        
    def ExtractMax(self):

        if len(self.heap) != 0: 
            ex_max = max(self.heap)
            indx = self.heap.index(ex_max) 
            self.heap.pop(indx) 
            self.MaxHeapify(ex_max) 
        return ex_max
        
    def IncreaseValue(self, i, value):

        if(i <= self.heap.count()):
            if(self.heap[i] < value):
                self.heap[i] = value
                self.MaxHeapify(self.heap, i)
    
    def Insert(self, value):

        self.heap.append(value)
        self.MaxHeapify(len(self.heap)-1)
        
    def MaxHeapify(self, i):

        l = 2*i 
        r = 2*i+1 
        if l < self.Size() and self.heap[l] > self.heap[i]:
            largest = r
        else:
            largest = i
          
        if r < self.Size() and self.heap[r] > self.heap[largest]:
            largest = r
            
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.MaxHeapify(self.heap, largest)
          
class MinHeap:

    def __init__(self):

        self.heap = []
        
    def Size(self):

        return len(self.heap)
    
    def Min(self):

        min_el = self.heap[0]
        for x in range (self.Size()):
          if self.heap[x] < min_el:
               min_el = self.heap[x]
        return min_el


    def ExtractMin(self):

        if len (self.heap) != 0:
            ex_min = min(self.heap)
            indx = self.heap.index(ex_min)
            self.heap.pop(indx)
            self.MinHeapify(ex_min)
        return ex_min
      
    def DecreaseValue(self, i, value):

        if(i <= self.heap.count()):
            if(self.heap[i] > value):
                self.heap[i] = value
                self.MinHeapify(self.heap, i)

    def Insert(self, value):

        self.heap.append(value)
        self.MinHeapify(len(self.heap)-1)


    def MinHeapify(self, i):

        l = 2*i
        r = 2*i+1
        if l < self.Size() and self.heap[l] < self.heap[i]:
            largest = l
        else:
            largest = i
          
        if r < self.Size() and self.heap[r] < self.heap[largest]:
            largest = r
            
        if largest != i: 
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.MaxHeapify(self.heap, largest)


H_low = MaxHeap() 
H_high = MinHeap()

def GetMedian(value):

    global H_low
    global H_high

    if value <= H_low.Max():
        H_low.Insert(value)
    else:
        H_high.Insert(value)
        
    if H_low.Size() >= H_high.Size() + 2:
        m = H_low.ExtractMax()
        H_high.Insert(m)
    elif H_high.Size() >= H_low.Size() + 2:
        m = H_high.ExtractMin()
        H_low.Insert(m)
     

    if (H_low.Size() + H_high.Size())%2 == 0:
        return H_low.Max(), H_high.Min()

    elif H_low.Size() > H_high.Size():
        return H_low.Max() 
    else:
        return H_high.Min() 

def main():
    file = open("MyInput.txt")
    n = int(file.readline())
    array = []
    for el in islice(file, 0, n):
        array.append(int(el))
    file.close

    file_res = open('MyOutput.txt', 'w')
    for i in range(n):
        file_res.write(str(GetMedian(array[i]))+"\n")
    file_res.close()
if __name__=="__main__":
    main()
