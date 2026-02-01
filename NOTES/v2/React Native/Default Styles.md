
---

# **View**

| Name            | Value      |
| --------------- | ---------- |
| `display`       | `flex`     |
| `flexDirection` | `column`   |
| `position`      | `relative` |

---

# **Text**

| Name        | Value     |
| ----------- | --------- |
| `alignSelf` | `stretch` |

---

# **Text Input**

| Name     | Value                      |
| -------- | -------------------------- |
| `height` | `48` (what it seems to be) |

---

# **ScrollView**

This element will automatically put the following properties on its direct children...

For a vertical `ScrollView`...

| Name        | Value     | Meaning                                                                         |
| ----------- | --------- | ------------------------------------------------------------------------------- |
| `alignSelf` | `stretch` | Each direct child element is forced to be at least as wide as the `ScrollView`. |
| `minWidth`  | `100%`    | Each direct child element is forced to be at least as wide as the `ScrollView`. |

For a horizontal `ScrollView`...

| Name        | Value     | Meaning                                                                         |
| ----------- | --------- | ------------------------------------------------------------------------------- |
| `alignSelf` | `stretch` | Each direct child element is forced to be at least as tall as the `ScrollView`. |
| `minHeight` | `100%`    | Each direct child element is forced to be at least as tall as the `ScrollView`. |

In order to counteract this behavior, you can apply `alignItems: center` on the `contentContainerStyle` of the `ScrollView`

---
