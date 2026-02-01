
---

# Description

- The `@Scope` annotation is used to specify the scope of a bean.

---

# Scope Values

| Scope Value | Description                                                      |
| ----------- | ---------------------------------------------------------------- |
| `singleton` | returns the same instance of a bean each time the bean is called |
| `prototype` | returns a new instance of a bean each time the bean is called    |

---

# Examples

``` java
public class MyBean {}

@Configuration
public class MyApplication
{
	@Bean
	@Scope("singleton")
	public MyBean singletonBean() {
		return new MyBean();
	}
	
	@Bean
	@Scope("prototype")
	public MyBean prototypeBean() {
		return new MyBean();
	}
}
```