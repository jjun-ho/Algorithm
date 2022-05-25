from random import randint

def insertionSort_ASC(arr, first, last, h):
    i = first + h
    while i <= last:
        val = arr[i]
        pos = i
        while pos > first and arr[pos - h] > val:
            arr[pos] = arr[pos - h]
            pos -= h
        arr[pos] = val
        i += h


def shellSort_ASC(arr,h):
    n = len(arr)
    while h > 0:
        for i in range(0, h):
            insertionSort_ASC(arr, i, n - 1, h)
        h //= 2
    return arr

array = [randint(1, 1000) for i in range(100)]

print('Shell Sort(57) :', shellSort_ASC(array,57));
print('Shell Sort(23) :', shellSort_ASC(array,23));
print('Shell Sort(10) :', shellSort_ASC(array,10));
print('Shell Sort(04) :', shellSort_ASC(array,4));
print('Shell Sort(01) :', shellSort_ASC(array,1));