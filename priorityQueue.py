import time

class Task:
    # Task class to represent a task with ID, priority, arrival time, and deadline
    def __init__(task, task_id, priority, arrival_time=None, deadline=None): # Using __init__ function for auto-invocation
        task.task_id = task_id  # Unique identifier for the task
        task.priority = priority  # Priority value (lower is higher priority in min-heap)
        task.arrival_time = arrival_time if arrival_time else time.time()  # Time task was added
        task.deadline = deadline  # Optional deadline for the task
    
    def __lt__(task, other): # using built-in "less than" comparator method for priority comparison
        return task.priority < other.priority  

class PriorityQueue:
    # Priority queue implemented as a binary heap
    def __init__(queue, is_max_heap=False): # Using __init__ method for automatic invocation
        queue.heap = []  # List to store heap elements
        queue.is_max_heap = is_max_heap  # Boolean to determine if it's a max-heap or min-heap
    
    def insert(queue, task):
        # Insert a new task into the heap
        if queue.is_max_heap:
            task.priority = -task.priority  # Convert to max-heap by negating priorities
        queue.heap.append(task)  # Add task to the end of the heap
        queue.heapify_up(len(queue.heap) - 1)  # Restore heap property
    
    def extract(queue):
        # Remove and return the highest/lowest priority task
        if queue.is_empty():
            return None
        queue.swap(0, len(queue.heap) - 1)  # Swap root with last element
        task = queue.heap.pop()  # Remove last element (former root)
        queue.heapify_down(0)  # Restore heap property
        if queue.is_max_heap:
            task.priority = -task.priority  # Restore original priority
        return task
    
    def adjust_key(queue, task_id, new_priority):
        # Modify the priority of an existing task
        for i, task in enumerate(queue.heap):
            if task.task_id == task_id:
                if queue.is_max_heap:
                    new_priority = -new_priority  # Adjust for max-heap
                queue.heap[i].priority = new_priority  # Update priority
                queue.heapify_up(i)  # Re-adjust heap upwards
                queue.heapify_down(i)  # Re-adjust heap downwards
                return
    
    def is_empty(queue):
        # Check if the heap is empty
        return len(queue.heap) == 0
    
    def heapify_up(queue, index):
        # Restore heap property by moving element up
        parent = (index - 1) // 2
        while index > 0 and queue.heap[index] < queue.heap[parent]:
            queue.swap(index, parent)
            index = parent
            parent = (index - 1) // 2
    
    def heapify_down(queue, index):
        # Restore heap property by moving element down
        size = len(queue.heap)
        while True:
            left = 2 * index + 1  # Left child index
            right = 2 * index + 2  # Right child index
            smallest = index  # Assume current index is smallest
            if left < size and queue.heap[left] < queue.heap[smallest]:
                smallest = left
            if right < size and queue.heap[right] < queue.heap[smallest]:
                smallest = right
            if smallest == index:
                break  # Heap property satisfied
            queue.swap(index, smallest)
            index = smallest
    
    def swap(queue, task1, task2):
        # Swap two elements in the heap
        queue.heap[task1], queue.heap[task2] = queue.heap[task2], queue.heap[task1]
