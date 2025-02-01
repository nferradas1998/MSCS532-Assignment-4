import time

class Task:
    # Task class to represent a task with ID, priority, arrival time, and deadline
    def __init__(task, task_id, priority, arrival_time=None, deadline=None): # Using __init__ function for auto-invocation
        task.task_id = task_id  # Unique identifier for the task
        task.priority = priority  # Priority value (lower is higher priority in min-heap)
        task.arrival_time = arrival_time if arrival_time else time.time()  # Time task was added
        task.deadline = deadline  # Optional deadline for the task
    
    def __lt__(self, other):
        return self.priority < other.priority  # Min-heap comparison (lower priority first)

    def __repr__(self):
        return f"Task(ID: {self.task_id}, Priority: {self.priority}, Arrival: {self.arrival_time}, Deadline: {self.deadline})"

class PriorityQueue:
    # Priority queue implemented as a binary heap
    def __init__(self, is_max_heap=False):
        self.heap = []  # List to store heap elements
        self.is_max_heap = is_max_heap  # Boolean to determine if it's a max-heap or min-heap
    
    def insert(self, task):
        # Insert a new task into the heap
        if self.is_max_heap:
            task.priority = -task.priority  # Convert to max-heap by negating priorities
        self.heap.append(task)  # Add task to the end of the heap
        self._heapify_up(len(self.heap) - 1)  # Restore heap property
    
    def extract(self):
        # Remove and return the highest/lowest priority task
        if self.is_empty():
            return None
        self._swap(0, len(self.heap) - 1)  # Swap root with last element
        task = self.heap.pop()  # Remove last element (former root)
        self._heapify_down(0)  # Restore heap property
        if self.is_max_heap:
            task.priority = -task.priority  # Restore original priority
        return task
    
    def increase_decrease_key(self, task_id, new_priority):
        # Modify the priority of an existing task
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                if self.is_max_heap:
                    new_priority = -new_priority  # Adjust for max-heap
                self.heap[i].priority = new_priority  # Update priority
                self._heapify_up(i)  # Re-adjust heap upwards
                self._heapify_down(i)  # Re-adjust heap downwards
                return
    
    def is_empty(self):
        # Check if the heap is empty
        return len(self.heap) == 0
    
    def _heapify_up(self, index):
        # Restore heap property by moving element up
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            index = parent
            parent = (index - 1) // 2
    
    def _heapify_down(self, index):
        # Restore heap property by moving element down
        size = len(self.heap)
        while True:
            left = 2 * index + 1  # Left child index
            right = 2 * index + 2  # Right child index
            smallest = index  # Assume current index is smallest
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == index:
                break  # Heap property satisfied
            self._swap(index, smallest)
            index = smallest
    
    def _swap(self, i, j):
        # Swap two elements in the heap
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def __repr__(self):
        return str(self.heap)

# Example Usage
pq = PriorityQueue(is_max_heap=True)  # Create a max-heap priority queue

pq.insert(Task(1, 5))  # Insert task with priority 5
pq.insert(Task(2, 1))  # Insert task with priority 1
pq.insert(Task(3, 8))  # Insert task with priority 8
pq.insert(Task(4, 3))  # Insert task with priority 3

print("Priority Queue after insertions:", pq)
print("Extracted task:", pq.extract())  # Extract highest priority task
pq.increase_decrease_key(2, 10)  # Modify priority of task ID 2
print("Priority Queue after modifying priority:", pq)
