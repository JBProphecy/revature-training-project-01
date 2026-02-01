
---

# Related to Multithreading

- The Producer-Consumer problem is a classic example of a multi-process synchronization problem.
- Here, we have a _fixed-size buffer_ and two classes of threads - _producers_ and _consumers_.
    - Producers produces the data to the queue
    - Consumers consume the data from the queue.
    - Both producer and consumer shares the same fixed-size buffer as a queue.
- The producer should produce data only when the queue is not full.
    - If the queue is full, then the producer shouldn't be allowed to put any data into the queue.
- The consumer should consume data only when the queue is not empty.
    - If the queue is empty, then the consumer shouldn't be allowed to take any data from the queue.
- We can solve the Producer-Consumer problem by using `wait()` & `notify()`methods to communicate between producer and consumer threads
    - The `wait()` method to pause the producer or consumer thread depending on the queue size.
    - The `notify()` method sends a notification to the waiting thread.
- Producer thread will keep on producing data for Consumer to consume.
- It will use `wait()` method when Queue is full and use `notify()` method to send notification to Consumer thread once data is added to the queue.

---

# Related to HashMap and TreeMap

`HashMap` is a Map which:

- Stores elements in key-value pairs
- Insertion/Retrieval of element by key is fast
- Tradeoff is that it does not maintain the order of insertion
- Permits one null key and null values

---

`TreeMap` is a Map whose:

- Keys are stored in a Sorted Tree structure
- Main benefit is that keys are always in a sorted order
- Insertion/Retrieval are slow
- Cannot contain null keys as null cannot be compared for sorting

---

`HashTable` is an older, thread-safe implementation of a `HashMap`. It does not allow null keys or null values.

---

# Related to ArrayList and LinkedList

|ArrayList|LinkedList|
|---|---|
|ArrayList internally uses a dynamic array to store the elements.|LinkedList internally uses a doubly linked list to store the elements.|
|Manipulation with ArrayList is slow because it internally uses an array. If any element is removed from the array, all the other elements are shifted in memory.|Manipulation with LinkedList is faster than ArrayList because of the use of nodes where you just need to change the nearest references of a node.|
|An ArrayList class can act as a list only because it implements List only.|LinkedList class can act as a list and queue both because it implements List and Deque interfaces.|
|ArrayList is better for storing and accessing data.|LinkedList is better for manipulating data.|
|The memory location for the elements of an ArrayList is contiguous.|The location for the elements of a linked list is not contiguous.

---

# Related to Queue and Deque

| Implementation          | Queue | Deque | Thread-safe | Allows nulls |
| ----------------------- | :---: | :---: | :---------: | :----------: |
| `LinkedList`            |   ✅   |   ✅   |      ❌      |      ✅       |
| `PriorityQueue`         |   ✅   |   ❌   |      ❌      |      ❌       |
| `ArrayDeque`            |   ✅   |   ✅   |      ❌      |      ❌       |
| `ConcurrentLinkedQueue` |   ✅   |   ❌   |      ✅      |      ✅       |
| `LinkedBlockingQueue`   |   ✅   |   ❌   |      ✅      |      ❌       |
| `ConcurrentLinkedDeque` |   ❌   |   ✅   |      ✅      |      ✅       |
| `LinkedBlockingDeque`   |   ❌   |   ✅   |      ✅      |      ❌       

---
