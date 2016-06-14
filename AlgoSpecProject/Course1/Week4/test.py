from Course1.Week4.sorting import partition3

arr = [2,2,3,3,1,1,4,4]
m1, m2 = partition3(arr, 0, len(arr)-1)
print(m1 ,m2, arr[m1], arr[m2])
print(arr)

