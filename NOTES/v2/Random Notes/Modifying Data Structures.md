
---

# Modifying Array-Based Data Structures

**Inserting an Element**
You'll need to make a new array of the original length plus one, and then copy over the beginning of the original array, then insert the new element, and then copy over the end of the original array, and then reassign the reference of the reference variable so that it points to the new array.

---

# Modifying Node-Based Data Structures

**Inserting a Node**
1. Create a new node and make it point to a node (the next node).
2. Change the reference of the previous node to point to the new node.

---
