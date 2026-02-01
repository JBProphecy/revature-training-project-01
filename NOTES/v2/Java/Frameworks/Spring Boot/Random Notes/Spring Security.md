
---

# Video

https://www.youtube.com/watch?v=nhsdPVXhbHo

---

# Dependency

``` xml
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

---

# Annotations

| Annotation              | Link |
| ----------------------- | ---- |
| `@EnableMethodSecurity` |      |
| `@EnableWebSecurity`    |      |
| `@PreAuthorize`         |      |
| `@Secured`              |      |

---

# Notes

- Security Filter Chain
	- guards at the door
- User Details Service
	- how to look up user from my database
- Password Encoder
	- BCrypt
	- take a raw password
	- hash it using the encoder
	- compare it to the stored password

---
