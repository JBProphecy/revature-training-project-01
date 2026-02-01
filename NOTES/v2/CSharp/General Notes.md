
---
# C\# Overview

C# is an object-oriented programming language.

C# is a compiled language.

C# is strongly and statically typed.

C# has garbage collection, so memory management is automatic.

---
# Compilation

C# code is compiled to IL (Intermediate Language) and executed in a .NET VM (Virtual Machine).

---
# Console

``` c#
Console.WriteLine("some text");
```

---
# Variables and Constants

You can define variables and constants. Each one must have a unique **`identifier`** (name).
When you define a variable, you can assign a value to it then or at another time.
When you define a constant, you must assign a value to it then.

``` c#
int myVariable; // variable definition (value not assigned)
myVariable = 5; // value assigned
myVariable = 8; // value changed
```

``` c#
int myVariable = 5; // variable definition (value assigned)
myVariable = 8; // value changed
```

``` c#
const int myConstant = 5; // constant definition (value assigned)
```

---
# Console

- `Console.Title`
- 