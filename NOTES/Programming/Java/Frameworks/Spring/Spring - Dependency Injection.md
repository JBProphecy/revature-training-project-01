
---

# Dependency Injection in Spring

In Spring, dependency injection is a central principle.

---

# Types of Dependency Injection

| Type                  | Description                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------ |
| Constructor Injection | the process of setting a dependency by passing it into the constructor for a class                     |
| Setter Injection      | the process of setting a dependency by passing it into a setter of an object.                          |
| Field Injection       | the process of setting a dependency by directly manipulating a field / instance variable of an object. |

---

# Ways to Configure Beans/Dependency Injection

There are 3 main ways to configure beans:

| Method                         | Description                                      |
| ------------------------------ | ------------------------------------------------ |
| XML-based configuration        | You configure beans in an XML file.              |
| annotation-based configuration | You use annotations to configure beans.          |
| Java-based configuration       | You use Java classes/methods to configure beans. |

---

# XML-Based Configuration

[[Spring - XML-Based Configuration]]

``` java
ApplicationContext XMLContext = new ClassPathXmlApplicationContext("my-file.xml");
```

---

# Java-Based Configuration

``` java
@Configuration
public class MyClass {
	@Bean
	public Animal getRandomAnimal() {
		// return some instance of the Animal class
	}
}
```

``` java
ApplicationContext JavaContext = new AnnotationConfigApplicationContext(MyClass.class);
```

---

