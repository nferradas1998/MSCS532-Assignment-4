def heapify(arr, n, i): # function to rearrange the elements of the heap
    largest = i  # Assume current node is the largest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than current largest
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree


def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):  # Start from last non-leaf node
        heapify(arr, n, i)


def heapsort(arr):
    n = len(arr)
    build_max_heap(arr) # Build a max heap

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap max element with last element
        heapify(arr, i, 0)  # Maintain max-heap property on reduced heap



arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
heapsort(arr)
print("Sorted array:", arr)
