
---

# Data Types

| Basic Type | Nullable Form |
| ---------- | ------------- |
| `Byte`     | `Byte?`       |
| `Short`    | `Short?`      |
| `Int`      | `Int?`        |
| `Long`     | `Long?`       |
| `Float`    | `Float?`      |
| `Double`   | `Double?`     |
| `Boolean`  | `Boolean?`    |
| `Char`     | `Char?`       |
| `String`   | `String?`     |

| Basic Type  | Mutable Form       |
| ----------- | ------------------ |
| `Array<T>`  |                    |
| `List<T>`   | `MutableList<T>`   |
| `Set<T>`    | `MutableSet<T>`    |
| `Map<K, V>` | `MutableMap<K, V>` |

| Type      |
| --------- |
| `Unit`    |
| `Any`     |
| `Nothing` |
| `Pair`    |
| `Triple`  |

---

``` kotlin
fun main() {
	println("Hello World")
	val a: Int = 5
	val b: Float = 5f
	val c: Float = 3.45f
	val d: Double = 7.24
	val e = true
	val f: Boolean = false
}
```

---

# Variables / References

| Keyword | Description                              |
| ------- | ---------------------------------------- |
| `val`   | declares an immutable reference/variable |
| `var`   | declares a mutable reference/variable    |

---

# Arithmetic Operators

| Operator | Function       |
| -------- | -------------- |
| `+`      | addition       |
| `-`      | subtraction    |
| `*`      | multiplication |
| `/`      | division       |
| `%`      | modulo         |

---

# Increment / Decrement

There are two types of increment/decrement: pre and post.

In the table below, `x` represents an integral value.

| Type           | Formula |
| -------------- | ------- |
| pre-increment  | `++x`   |
| pre-decrement  | `--x`   |
| post-increment | `x++`   |
| post-decrement | `x--`   |

---

# Comparison Operators

| Operator | Function                      |
| -------- | ----------------------------- |
| `==`     | is equal to (structural)      |
| `!=`     | is not equal to (structural)  |
| `===`    | is equal to (referential)     |
| `!==`    | is not equal to (referential) |
| `>`      | is greater than               |
| `<`      | is less than                  |
| `>=`     | is greater than or equal to   |
| `<=`     | is less than or equal to      |

---

# Equality

| Kotlin Implementation | Description          | Java Implementation |
| --------------------- | -------------------- | ------------------- |
| `==`                  | structural equality  | `.equals()`         |
| `===`                 | referential equality | `==`                |

---

# Logical Operators

| Operator | Function |
| -------- | -------- |
| `!`      | NOT      |
| `&&`     | AND      |
| `\|\|`   | OR       |

---

``` kotlin
val input: String = readln()
println("You've entered $input")
```

---
