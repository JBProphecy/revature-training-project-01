
---

# Notes (Revature)

- The Singleton design pattern allows for the creation of a single instance of an object in memory that can be shared across multiple classes.
- Benefits of using a Singleton include coordination across the system, clear instance retrieval, control over instantiation, and global access point.
- Situations where Singleton pattern can be useful include logging frameworks, database connections, caching, configuration settings, and thread pool/task manager in concurrent programming.

To make a class into a Singleton in Java:

1. `private static` variable of the class' type
2. `private` constructor - to prevent arbitrary object creation
3. `public static getInstance()` method, which will either instantiate the object or return the instance in memory

---

# Example (Revature)

``` java
public class Singleton {
	private static Singleton instance;

	private Singleton() {}

	public static Singleton getInstance() {
		if (instance == null) { instance = new Singleton(); }
		return this.instance;
	}
}
```

---
