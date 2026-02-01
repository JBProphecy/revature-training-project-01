
---

# XML-Based Configuration Notes

- In Spring, beans and their dependencies can be configured in an XML file.
	- The file is often named `applicationContext.xml`
	- The file is often placed in the `src/main/resources` directory.
	- The full path would be `src/main/resources/applicationContext.xml`.

---

- In the XML configuration file, each bean is defined with the `<bean>` tag.
	- The `id` attribute is used to identify the bean.
	- The `class` attribute is used to specify the class of the bean.

``` xml
<bean id="exampleBean" class="com.example.ExampleBean" />
```

---

- For constructor-based dependency injection, the `<constructor-arg>` tag is used.
	- The `ref` attribute is used to specify which bean should be injected.

``` xml
<bean id="constructorBean" class="com.example.ConstructorBean">
	<constructor-arg ref="exampleBean">
</bean>
```

---

- For setter-based dependency injection, the `<property>` tag is used.
	- The `name` attribute is used to specify which property should receive the bean.
	- The `ref` attribute is used to specify which bean should be injected.

``` xml
<bean id="setterBean" class="com.example.SetterBean">
	<constructor-arg name="exampleBeanProperty" ref="exampleBean">
</bean>
```

---
