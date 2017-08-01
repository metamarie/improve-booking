/* text file                        */
/* This line has been added in Atom */

def swap(a, x, y):
    tmp = a[x]
    a[x] = a[y]
    a[y] = tmp
    return a

def bubble_sort(x):
    for i in range(len(x)):
        for k in range(len(x) - 1, i, -1):
            if x[k] < x[k - 1]:
                swap(x, k, k - 1)
    return x


