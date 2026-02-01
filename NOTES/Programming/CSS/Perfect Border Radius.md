
---

It's always been a pain in my ass when I want to have some border radius on an element and then some border radius on a child element inside of it, where there is some space between them.

What I would do is set the parent element with some border radius and some padding and maybe some border width. I would calculate the border radius for the child element from those values.

All I have to do is put padding on the child element and give it the same border radius as the parent element minus any border width on the parent.

---

I've since learned that the method I described above can lead to issues if the padding is not the same on all four sides.

---
## Real Solution

The best way to have perfect border radius is to calculate it manually. From the outer border radius, you subtract any border width and padding. From the inner border radius, you add any padding and border width.

Essentially, whatever element you put border radius on will have an outer edge and if it has any border width, it will have an inner edge of the border radius minus the border width.

---
