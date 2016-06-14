# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def ReadData2(self, arr):
    self._data = arr


  def Size(self):
      return len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def Parent(self, i):
    return i // 2

  def LeftChild(self, i):
    return 2*i

  def RightChild(self, i):
    return 2*i + 1

  def Swap(self, i, j):
    self._swaps.append((i,j))
    self._data[i], self._data[j] = self._data[j], self._data[i]


  def SiftDown(self,i):
    maxIndex = i
    l = self.LeftChild(i)
    if l < self.Size() and self._data[l] < self._data[maxIndex]:
        maxIndex = l
    r = self.RightChild(i)
    if r < self.Size() and self._data[r] < self._data[maxIndex]:
        maxIndex = r
    if i != maxIndex:
        self.Swap(i, maxIndex)
        self.SiftDown(maxIndex)

  def SiftUp(self, i):
    k = i
    while k > 1 and self._data[self.Parent(k)] > self._data[k]:
      self.Swap(self.Parent(k), k)
      k = self.Parent(k)

  def IsMinHeap(self, i):
    if i == 0:
      rootResult = True
      # check is children are ok
      if self.LeftChild(i) < len(self._data):
        if self._data[self.LeftChild(i)] < self._data[i]:
          rootResult = False
      if self.RightChild(i) < len(self._data):
        if self._data[self.RightChild(i)] < self._data[i]:
          rootResult = False
      return rootResult
    else:
      return self._data[self.Parent(i)] < self._data[i]

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    size = self.Size()

    for i in reversed(range(size // 2 + 1)):
        if not self.IsMinHeap(i):
            self.SiftDown(i)

    print(self._data)

  def Solve(self):
    #self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
