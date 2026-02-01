
---

When it comes to padding, border width, and border radius, they should all be based on the size of the element, not each other. By doing it that way, you can change the size of the element and they will all change relatively. If you have them based on one another, they will still change the same way as long as the the "root" is dependent on the element, but it's a little more difficult to work with. Unless you need the border radius to be exactly twice the size of the border width or something for example, just make each of those properties some percentage of say the element's height. you can change those values until it your element looks good and then whenever you change the size of the element, the proportions will remain the same and it should still look good. Additionally, since they are based on the size of the element and not rem, you don't have to worry about those values at all once you get them to look good. It's great that way.

---
