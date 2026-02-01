## Variables

To declare a variable means to give it a name.
To initialize a variable means to assign a value to it.

A variable must always have a name, but it may not always have a value assigned to it, which means a variable must always be declared, but it may not always be initialized.

An initialized variable is a variable that has been assigned a value.
An uninitialized variable is a variable that has not been assigned a value.

The declaration of a variable occurs at the time of its creation. Whether or not a variable must be initialized at that time depends on the method of its creation.

---

There are two common ways to create a variable.
1. You can create a variable by using the **const** keyword.
2. You can create a variable by using the **let** keyword.

---

A variable that's been declared with the **const** keyword has an immutable value, which means that value cannot be changed/reassigned. When you declare a variable with the **const** keyword, you must initialize it at that moment.

A variable that's been declared with the **let** keyword has a mutable value, which means that value can be changed/reassigned. When you declare a variable with the **let** keyword, you can initialize it at any time.

---

**Example Code**
1. const myName = "Jack";
2. console.log(myName);
3. let message;
4. console.log(message);
5. message = "first one";
6. console.log(message);
7. message = "second one";
8. console.log(message);
9. let myAge = 22;
10. console.log(myAge);

---

In the example code...

- The 1st line of code initializes a variable called **myName** with a value of "Jack".
- The 2nd line of code displays "Jack" in the the console.

- The 3rd line of code declares a variable called **message**.
- The 4th line of code displays undefined in the console.

- The 5th line of code assigns a value of "first one" to **message**.
- The 6th line of code displays "first one" in the console.

- The 7th line of code reassigns the value of **message** to "second one".
- The 8th line of code displays "second one" in the console.

- The 9th line of code initializes a variable called **myAge** with a value of 22.
- The 10th line of code displays 22 in the console.

---

Since the variable **message** is created/declared with the **let** keyword (line 3), it can be uninitialized initially as it is in line 3, it can be assigned a value or initialized later on as it is in line 5, and then its value can be reassigned as it is in line 7.

Since the variable **myName** is created/declared with the **const** keyword (line 1), it must be initialized as it is in line 1 and its value cannot be altered like the value of **message** is altered in lines 5 and 7.

The 9th line of code shows that variables created with the **let** keyword can be initialized initially in the same way that variables created with the **const** keyword are initialized initially as shown in line 1, but lines 3-8 show that variables created with the **let** keyword don't have to be initialized initially unlike variables created with the **const** keyword.

As shown in the console from line 4, when a variable is uninitialized or has not been assigned a value, its value is undefined.