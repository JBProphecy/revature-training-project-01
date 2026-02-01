
---
# Assignment Operator

| Operator | Performing | Verb Term | Formula | Phrase     |
| -------- | ---------- | --------- | ------- | ---------- |
| =        | assignment | equals    | a = b   | a equals b |

---
# Arithmetic Operators

| Operator | Performing          | Verb Term  | Formula | Phrase         |
| -------- | ------------------- | ---------- | ------- | -------------- |
| +        | addition            | plus       | a + b   | a plus b       |
| -        | subtraction         | minus      | a - b   | a minus b      |
| \*       | multiplication      | times      | a \* b  | a times b      |
| /        | division            | divided by | a / b   | a divided by b |
| %        | modulus / remainder | modulo     | a % b   | a modulo b     |

``` java
int a = 2 + 3; // (a == 5)
int b = 5 - 2; // (b == 3)
int c = 3 * 4; // (c == 12)
int d = 17 / 5; // (d == 3)
int e = 17 % 5 // (e == 2)
```

| Operator | Performing                    | Formula | Equivalency |
| -------- | ----------------------------- | ------- | ----------- |
| +=       | addition and assignment       | a += b  | a = a + b   |
| -=       | subtraction and assignment    | a -= b  | a = a - b   |
| \*=      | multiplication and assignment | a \*= b | a = a \* b  |
| /=       | division and assignment       | a /= b  | a = a / b   |
| %=       | modulus and assignment        | a %= b  | a = a % b   |

``` java
int a = 5; // (a = 5)
a += 3; // (a = 8)
```

``` java
int a = 5 // (a = 5)
a -= 3; // (a = 2)
```

``` java
int a = 5 // (a = 6)
a *= 4; // (a = 24)
```

``` java
int a = 23; // (a = 6)
a /= 3; // (a = 2)
```

``` java
int a = 17; // (a = 17)
a %= 5; // (a = 2)
```

---
# Comparison Operators

| Operator | Meaning                     | Formula |
| -------- | --------------------------- | ------- |
| ==       | is equal to                 | a == b  |
| !=       | is not equal to             | a != b  |
| >        | is greater than             | a > b   |
| <        | is less than                | a < b   |
| >=       | is greater than or equal to | a >= b  |
| <=       | is less than or equal to    | a <= b  |

---
# Logical Operators

| Operator | Performing  | Formula  |
| -------- | ----------- | -------- |
| &&       | Logical AND | a && b   |
| \|\|     | Logical OR  | a \|\| b |
| !        | Logical NOT | !a       |

---
# Bitwise Operators

| Operator | Performing             | Formula |
| -------- | ---------------------- | ------- |
| &        | Bitwise AND            | a & b   |
| \|       | Bitwise OR             | a \| b  |
| ^        | Bitwise XOR            | a ^ b   |
| ~        | Bitwise Complement     | ~a      |
| <<       | Left Shift             | a << b  |
| >>       | Right Shift (signed)   | a >> b  |
| >>>      | Right Shift (unsigned) | a >>> b |

---
# Increment / Decrement

| Operator | Performing | Type           | Formula |
| -------- | ---------- | -------------- | ------- |
| ++       | increment  | pre-increment  | ++a     |
|          |            | post-increment | a++     |
| --       | decrement  | pre-decrement  | --a     |
|          |            | post-decrement | a--     |

``` java
// example of pre-increment
int a = 5;
int b = ++a; // (a = 6) (b = 6)
```

``` java
// example of post-increment
int a = 5;
int b = a++; // (a = 6) (b = 5)
```

``` java
// example of pre-decrement
int a = 5;
int b = --b; // (a = 4) (b = 4)
```

``` java
// example of post-decrement
int a = 5;
int b = b--; // (a = 4) (b = 5)
```

---
