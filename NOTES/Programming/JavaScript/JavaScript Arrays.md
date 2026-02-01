In JavaScript, an array can be declared in two ways...

array = Array();

or

array = \[\];

---

Let's say you initialize an array like this...

array = \["a", "b", "c", "d"\];

The length of this array is 4.
You can access these elements with an index.

The index of the first element in an array is always 0, so in this case, array\[0\] refers to "a".

The index of the last element in an array is always equal to the length of the array minus one, unless the array has no elements, so in this case, array\[3\] refers to "d".

---
## Array Properties

**array.length**

This property represents the number of elements in an array, which can be referred to as its length, size, or cardinality.

---
## Array Methods

**array.includes(element)**

This method accepts one argument, which should be the element you want to search for in an array.

This method will return true or false depending on whether or not an array contains a specific element.

---

**array.push()**

This method will append elements to the end of an array and return its new length.

This method can accept any number of elements as arguments.

---

**array.pop()**

This method will remove the last element from an array and return that element.

If there are no elements in an array when this method is called, it will return undefined.

This method does not accept any arguments.

---

**array.unshift()**

This method will append elements to the beginning of an array and return its new length.

This method can accept any number of elements as arguments.

---

**array.shift()**

This method will remove the first element from an array and return that element.

If there are no elements in an array when this method is called, it will return undefined.

This method does not accept any arguments.

---

