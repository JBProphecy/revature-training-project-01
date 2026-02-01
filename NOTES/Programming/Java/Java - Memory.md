
---

There are two main types of memory used in Java applications: stack memory and heap memory. Stack memory is a smaller allocation of space, which is used to store local variables. Heap memory is a larger allocation of data, which stores the majority of data in Java applications.

If you create a primitive variable, the variable and the data will be stored in the stack.

If you create an object, the reference variable will be stored in the stack, but the actual data for the object will be stored in the heap. The reference variable in the stack points to the location of the object in the heap. You can have multiple variables pointing to the same object in the heap.

---
