import random
import time
import threading

def quick_sort(array):
    array_length = len(array)
    if array_length <= 1:
        return array
    else:
        pivot = array[0]
        greater = [ element for element in array[1:] if element > pivot ]
        lesser = [ element for element in array[1:] if element <= pivot ]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

def merge_sort(arr):
    top = []
    bottom = []
    while len(arr) > 1:
        top.append(arr.pop(arr.index(max(arr))))
        bottom.append(arr.pop(arr.index(min(arr))))
    if arr:
        bottom.append(arr[0])
    top.reverse()
    return bottom + top

def run_merge_sort():
    total_merge_time = 0
    merge_always_correct = []
    for i in range(1000):
        arr = [random.randint(0, 1000) for a in range(1000)]

        # Merge Sort time, and if it correctly sorted the array
        merge_started = time.time()
        merge_sorted = merge_sort(arr)
        total_merge_time += time.time() - merge_started
        merge_always_correct.append(is_sorted(merge_sorted))

    print(f"Total Merge Time: {total_merge_time}")
    print(f"Merge Always Correct: {all(merge_always_correct)}")

def run_quick_sort():
    total_quick_time = 0
    quick_always_correct = []
    for i in range(1000):
        arr = [random.randint(0, 1000) for a in range(1000)]
        # Quick Sort time, and if it correctly sorted the array
        quick_started = time.time()
        quick_sorted = quick_sort(arr)
        total_quick_time += time.time() - quick_started
        quick_always_correct.append(is_sorted(quick_sorted))

    print(f"Total Quick Time: {total_quick_time}")
    print(f"Quick Always Correct: {all(quick_always_correct)}")

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def main():
    t1 = threading.Thread(target=run_merge_sort, args=())
    t2 = threading.Thread(target=run_quick_sort, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
