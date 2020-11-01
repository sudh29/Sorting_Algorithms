# insertion sort
def insertionSort(a):
    n = len(a)
    for i in range(1, n):
        value = a[i]
        hole = i
        while hole > 0 and A[hole - 1] > value:
            a[hole] = a[hole - 1]
            hole -= 1
        a[hole] = value
    return a


A = [5, 2, 6, 7, 2, 1, 0, 3]
print(insertionSort(A))
