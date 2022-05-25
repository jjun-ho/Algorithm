from random import randint

def InsertionSort(list, first, last, h):
    i = first + h
    while i <= last:
        val = list[i]
        pos = i
        while pos > first and list[pos - h] > val:
            list[pos] = list[pos - h]
            pos -= h
        list[pos] = val
        i += h

def ShellSort(list,h):
    n = len(list)
    while h > 0:
        for i in range(0, h):
            InsertionSort(list, i, n - 1, h)
        h //= 2
    return list

rlist = [randint(1, 1000) for i in range(100)]

print('Shell_Sort(57) :', ShellSort(rlist,57))
print('Shell_Sort(23) :', ShellSort(rlist,23))
print('Shell_Sort(10) :', ShellSort(rlist,10))
print('Shell_Sort(04) :', ShellSort(rlist,4))
print('Shell_Sort(01) :', ShellSort(rlist,1))