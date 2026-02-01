
---

Let's say you have a `Text` element nested inside in a `View` element.

``` tsx
<View>
  <Text>Example</Text>
</View>
```

By default, `View` has `flexDirection` = `column` and `Text` has `alignSelf` = `stretch`. As a result, `Text` will occupy the full width of `View`.

if `View` has `flexDirection` = `column`, `Text` will occupy the full width of `View`.
If `View` has `flexDirection` = `row`, `Text` will occupy the full height of `View`.

This behavior takes place because `alignSelf` (on the child `Text`) overrides `alignItems` (on the parent `View`) for that specific element, and `alignItems` influences the behavior of child elements on the cross-axis.

**Relevant Defaults**

| Element | Property Name   | Property Value |
| ------- | --------------- | -------------- |
| `View`  | `display`       | `flex`         |
| `View`  | `flexDirection` | `column`       |
| `Text`  | `alignSelf`     | `stretch`      |

**Table of Effects**

| `flexDirection` on `View` | `alignSelf` on `Text` | Resulting Behavior                                                              |
| ------------------------- | --------------------- | ------------------------------------------------------------------------------- |
| `column`                  | `stretch`             | `Text` will occupy the full width of `View`                                     |
| `row`                     | `stretch`             | `Text` will occupy the full height of `View`                                    |
| `column`                  | `flex-start`          | `Text` will occupy its natural width and be positioned at the start of `View`   |
| `row`                     | `flex-start`          | `Text` will occupy its natural height and be positioned at the start of `View`  |
| `column`                  | `center`              | `Text` will occupy its natural width and be positioned in the center of `View`  |
| `row`                     | `center`              | `Text` will occupy its natural height and be positioned in the center of `View` |
| `column`                  | `flex-end`            | `Text` will occupy its natural width and be positioned at the end of `View`     |
| `row`                     | `flex-end`            | `Text` will occupy its natural height and be positioned at the end of `View`    |

---
