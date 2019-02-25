def optimized_bubble_sort(arr):
    """
    Here basically we keep track of the last index where we did swapping which tell us
    everything after that index is already sorted so no need to repeat the process of
    comparison. Therefore, every loop, we decrement our second loop range, n, depending
    where the last swap happened.
    """
    n = len(arr)
    swap = False
    while n > 1:
        for j in range(1, n, 1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j-1]
                last_swap_index = j
                swap = True
        if swap:
            n = last_swap_index
            swap = False

        else:
            break
    return arr
arr = []
import random
for i in range(1_000_001):
    arr.append(random.randint(1, 1_000_000))

arr = optimized_bubble_sort(arr)
for i, a in enumerate(arr):
    print(i, a)
