"""

https://en.wikipedia.org/wiki/Bubble_sort

Worst-case performance: O(N^2)

If you call bubble_sort(arr,True), you can see the process of the sort
Default is simulation = False

"""


def bubble_sort(arr, simulation=False):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    iteration = 0
    if simulation:
        print(f"iteration {iteration}:", *arr)
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for k in range(1, n-x):
            if arr[k - 1] > arr[k]:
                swap(k - 1, k)
                swapped = True
                if simulation:
                    iteration = iteration + 1
                    print(f"iteration {iteration}:", *arr)
                    
    return arr
