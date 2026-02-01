
---

# Getting Started

- https://spring.io/guides/gs/spring-boot
- https://start.spring.io/

---

# Configuration - Properties File

- **Name:** `application.properties`
- **Location:** `src/main/resources`

``` properties
spring.application.name=MySpringBootApp
server.port=8080
```

---

# Configuration - YAML File

- **Name:** `application.yaml`
- **Location:** `src/main/resources`

``` yaml
spring:
  application:
    name: SpringBootDemo
server:
  port: 8080
```

---

# Configuration Precedence

- Regarding the two configuration methods for Spring Boot (with a properties file or with a YAML file), the properties file will take precedence over the YAML file.

---

# Example Code


``` java
import java.util.Arrays;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class App
{
	@Value("${spring.application.name}")
	private String appName;
	public static void main(String[] args) {
		SpringApplication.run(App.class, args);
	}
	
	@Bean
	public CommandLineRunner inspectorBean(ApplicationContext ctx) {
		return args -> {
			System.out.println("Inspecting the beans provided by Spring Boot:");
			String[] beanNames = ctx.getBeanDefinitionNames();
			Arrays.sort(beanNames);
			for (String beanName : beanNames) {
				System.out.println("Bean Name: " + beanName)
			}
		}
	}
}
```

---
