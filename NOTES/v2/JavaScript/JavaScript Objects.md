In JavaScript, an object is a non-primitive data type that stores key-value pairs.

In JavaScript, an object can be declared in two ways...

---

object = Object();

or

object = {};

---

Let's say you have an object with some key/value pairs...

object = {
	name: "Jack",
	age: 22
}

These values can be accessed in two ways: through dot notation or through bracket notation.

To access these values through dot notation, you can write this...

console.log(object.name);
console.log(object.age);

To access these values through bracket notation, you can write these lines...

console.log(object\[name\]);
console.log)object\[age\]);

---

In the example above, (name) and (age) are keys, and ("Jack") and (22) are values.

If a key in an object has a space in its name, you must surround it with quotes like this...

object = {
	name: "Jack",
	age: 22,
	"space key": 88
}

---

