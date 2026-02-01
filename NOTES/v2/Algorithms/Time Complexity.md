
---

# Time Complexity Notes

- The time it takes for an algorithm to run from start to finish can be called its execution time.

- The execution time of an algorithm can vary depending on the amount of data it will process, the current state of that data, and processing power of the machine that will run the algorithm.

- The time complexity of an algorithm is a set of functions that...
	- describe how an algorithm will perform given the size of an input.
	- describe the execution time of an algorithm given the size of an input.
	- describe how long it will take for an algorithm to execute given the size of an input.

- When computing the time complexity of an algorithm:
	- The processing power of the machine running it can be ignored.
	- The amount of data provided to it can be controlled.
	- The nature of the algorithm (how it handles data) must be considered.
	- The possible states of the data provided to it must be considered.

- An algorithm will handle every acceptable dataset provided to it in the same way, but the degree of variability that can exist among those datasets can and will most likely affect the execution time of the algorithm. As a result, two different datasets may yield different execution times for the same algorithm.

- Regarding time complexity of an algorithm:
	- **`Big-Omega Notation`** is used to describe the best / fastest scenario.
	- **`Big-Theta Notation`** is used to describe the average scenario.
	- **`Big-O Notation`** is used to describe the worst / slowest scenario.

---

# Time Complexity Table

- This table describes the complexity of algorithms. From "constant" to "factorial", they are listed in order from smallest to largest... or best to worst.

- Regarding time complexity, a constant algorithm will require the least amount of time or while a factorial algorithm will require the most.

| Complexity Type | Big-Omega Notation (best) | Big-Theta Notation (average) | Big-O Notation (worst) |
| --------------- | ------------------------- | ---------------------------- | ---------------------- |
| constant        | $\Omega (1)$              | $\Theta (1)$                 | $\text{O} (1)$         |
| logarithmic     | $\Omega (\log(n))$        | $\Theta (\log(n))$           | $\text{O} (\log(n))$   |
| linear          | $\Omega (n)$              | $\Theta (n)$                 | $\text{O} (n)$         |
| linearithmic    | $\Omega (n \log(n))$      | $\Theta (n \log(n))$         | $\text{O} (n \log(n))$ |
| quadratic       | $\Omega (n^2)$            | $\Theta (n^2)$               | $\text{O} (n^2)$       |
| exponential     | $\Omega (2^n)$            | $\Theta (2^n)$               | $\text{O} (2^n)$       |
| factorial       | $\Omega (n!)$             | $\Theta (n!)$                | $\text{O} (n!)$        |

---
