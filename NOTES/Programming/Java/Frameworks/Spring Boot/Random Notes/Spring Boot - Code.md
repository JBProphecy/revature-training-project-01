
---

``` java
import java.util.Arrays;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class SpringbootdemoApplication {

	@Value("${spring.application.name}")
	private String appName;

	public static void main(String[] args) {
		SpringApplication.run(SpringbootdemoApplication.class, args);
	}

	@Bean
	public CommandLineRunner inspectorBean(ApplicationContext ctx) {
		return args -> {
			System.out.printf("Inspecting the Beans Provided by Spring Boot in %s:\n", this.appName);
			String[] beanNames = ctx.getBeanDefinitionNames();
			Arrays.sort(beanNames);
			Arrays.stream(beanNames)
				.forEach(beanName -> System.out.println("Bean Name: " + beanName));
			System.out.println("Finished Inspecting the Beans Provided by Spring Boot");
		};
	}
}
```

---

# App Name Variable from Configuration

``` java
@Value("${spring.application.name}")
private String appName;
```

# Main Method

``` java
public static void main(String[] args) {
	SpringApplication.run(SpringbootdemoApplication.class, args);
}
```

---

# Inspector Bean

``` java
@Bean
public CommandLineRunner inspectorBean(ApplicationContext ctx) {
	return args -> {
		System.out.printf("Inspecting the Beans Provided by Spring Boot in %s:\n", this.appName);
		String[] beanNames = ctx.getBeanDefinitionNames();
		Arrays.sort(beanNames);
		Arrays.stream(beanNames)
			.forEach(beanName -> System.out.println("Bean Name: " + beanName));
		System.out.println("Finished Inspecting the Beans Provided by Spring Boot");
	};
}
```

---
