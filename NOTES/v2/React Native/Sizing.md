
---

## **Important**

Using `StyleSheet.absoluteFill`, which corresponds to an object that looks like this...

``` json
{
	position: "absolute",
	left: 0,
	right: 0,
	top: 0,
	bottom: 0
}
```

will make that element occupy the dimensions of the `padding-box` of its parent element.

Using `width: 100%` and `height: 100%` on an element will make either the `content-box` or the `border-box` of that element stretch to occupy the dimensions of the `content-box` of the parent element, depending on whether `boxSizing` on that element is `content-box` or `border-box`.

Using `flex: 1` on an element will make that element stretch to occupy the dimensions of the `content-box` of its parent element, specifically along the `main-axis` of the parent element. This will take priority over `width` or `height`, along the `main-axis`.

Using `width: auto` or `height: auto` on an element will do two things...

- The `margin-box` of that element will stretch to fit the `content-box` of the parent element along the `cross-axis` of the parent element.

- The `content-box` of that element will shrink to fit the total size of its children along the `main-axis` of the parent element.

Using `flex: 1` on an element will make the `margin-box` of that element stretch to fit the `content-box` of the parent element along the `main-axis` of the parent element.

## **Summary**

When you have a single element as the only child of an element, you can use `flex: 1` to make the `margin-box` of that element fit the `content-box` of the parent element. This happens for four reasons...

- `flex: 1` will make the `margin-box` of that element stretch to fit the `content-box` of the parent element along the `main-axis` of the parent element.

- When the `width` of an element is undefined, its default value is `auto`.
- When the `height` of an element is undefined, its default value is `auto`.

- No matter what the `flexDirection` of the parent element is, the dimension of the child element along the `main-axis` of the parent element will be influenced by `flex: 1` and the dimension of the child element along `cross-axis` of the parent element will be influenced by either `width: auto` or `height: auto`, whichever one corresponds to that dimension along the `cross-axis`.

- `auto` will make the `margin-box` of that element stretch to fit the `content-box` of the parent element along the `cross-axis` of the parent element.

---

# **View**

Without any styles, the `width` and `height` of a `View` are effectively `auto`, which means the `View` its dimensions will be intrinsic. Without any children, the `View` will collapse and have zero size.

---

| Name     | Value       | Implicitly | Meaning                                                  |
| -------- | ----------- | ---------- | -------------------------------------------------------- |
| `width`  | `undefined` | `auto`     | its width will be intrinsic unless influenced by parent  |
| `height` | `undefined` | `auto`     | its height will be intrinsic unless influenced by parent |

---

## **Default Flex Properties of a View**

A `View` is a flex-container by default.

| Name              | Value     | Meaning                                                        |
| ----------------- | --------- | -------------------------------------------------------------- |
| `flexDirection`   | `column`  | the main-axis is vertical - its children will align vertically |
| `alignItems`      | `stretch` | its children will occupy the full length cross-axis            |
| `justify-content` | `center`  | its children will align to the start of the cross-axis         |
| `flex-shrink`     | `0`       | it                                                             |

---

# **Using Percentages for Size**

Normally, when  the `width` or `height` of an element is a percentage value, its `width` or `height` will be computed relative to the content-box of its parent.

---

# **Important Flex Rules**

The property `flex` is shorthand for the properties `flex-grow`, `flex-shrink`, and `flex-basis`.

If `flex-grow > 0` or `flex-shrink > 0` for an element, the `width` or `height` of the element will be ignored. The dimension of the element that will be ignored depends on the `flex-direction` of its parent.

---
