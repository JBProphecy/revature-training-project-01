
---

| Annotation                 | Description                                                                                                                 |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `@NoArgsConstructor`       | Used on a class to generate a constructor with no parameters.                                                               |
| `@RequiredArgsConstructor` | Used on a class to generate a constructor with a parameter for each final field.                                            |
| `@AllArgsConstructor`      | Used on a class to generate a constructor with a parameter for each field.                                                  |
| `@Getter`                  | If used on a class, it will generate a getter for each field. If used on a field, it will generate a getter for that field. |
| `@Setter`                  | If used on a class, it will generate a setter for each field. If used on a field, it will generate a setter for that field. |
| `@ToString`                | Used on a class to generate a `toString` method for the class.                                                              |
| `@ToString.Exclude`        | Used at the field level to exclude a field from being included in the result of the `toString` method of the class.         |
| `@EqualsAndHashCode`       | Used on a class to generate both an `equals` method and a `hashCode` method for the class.                                  |
| `@Data`                    |                                                                                                                             |
| `@Value`                   |                                                                                                                             |

---

The `@Data` annotation is used at the class level to implement the following annotations:
- `@RequiredArgsConstructor`
- `@Getter`
- `@Setter`
- `@ToString`
- `@EqualsAndHashCode`

---

The `@Value` annotation is used at the class level to make an immutable class (the class is final and all of its fields are marked with private and final), implementing the following annotations:
- `@AllArgsConstructor`
- `@Getter`
- `@ToString`
- `@EqualsAndHashCode`

---
