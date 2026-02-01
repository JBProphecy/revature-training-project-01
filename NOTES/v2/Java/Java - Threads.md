
---

# Creating a Thread

You can create a new thread in one of two ways:

**Approach 1**
- Create a class that extends the Thread class.
	- Override the `run()` method.
- Create an instance of the new class, which is a subclass of the Thread class.
	- Call the `start()` method.

**Approach 2**
- Create a class that implements the Runnable interface.
	- Override the `run()` method.
- Create an instance of the Thread class by passing a new instance of the new class into its constructor.
	- Call the `start()` method.

---

# Key Differences

With the first approach, you can't extend any more classes because Java doesn't support multiple inheritance and the class is already extending the Thread class.

With the second approach, you still have the ability to extend a class, which makes the second approach more flexible.

---

# States of a Thread

| State           | Description |
| --------------- | ----------- |
| `NEW`           |             |
| `RUNNABLE`      |             |
| `BLOCKED`       |             |
| `WAITING`       |             |
| `TIMED_WAITING` |             |
| `TERMINATED`    |             |

---

In Java, you can get the current state of a thread by using the `getState()` method.

---

# Other Things

- synchronization
- deadlock
- live-lock
- producer-consumer problem

---
