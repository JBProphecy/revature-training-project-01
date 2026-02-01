
---

# Notes (Revature)

- The Factory pattern creates objects with unknown types until runtime, providing flexibility.
- Reasons to use the factory pattern include handling unknown types, hiding creational logic, enabling easy extension, and reusing objects.
- Benefits of the factory design pattern include adhering to a single responsibility and open/close principle, abstracting object creation from the user and encapsulating the object.
- Some situations where using a factory can be useful include Dependency injection frameworks, database access, logging frameworks, and GUI component creation in graphical user interface development.

---

# Example (Revature)

``` java
public interface Dessert {}

public class Cake extends Dessert {}

public class Cookie extends Dessert {}

public class IceCream extends Dessert {}

public class DessertNotFoundException extends RuntimeException {}

public class DessertFactory {
	public static Dessert getDessert(String type) {
		switch (type) {
			case "cake":
				return new Cake();
				break;
			case "cookie":
				return new Cookie();
				break;
			case "ice cream":
				return new IceCream();
				break;
			default:
				throw new DessertNotFoundException(type + " not found");
		}
	}
}
```

---
