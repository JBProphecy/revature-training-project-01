
---

# Definitions

- Gradle is a build tool used for Android development to automate the process of building and publishing apps.

---

# Key Concepts

- The Gradle Wrapper

---

# Commands

```
./gradlew tasks
```

---

# Custom Plugin Example

``` kotlin
class HelloWorldPlugin: Plugin<Project> {
	override fun apply(target: Project) {
		println("Hello World")
	}
}
apply<HelloWorldPlugin>()
```

---
