
# Notes

- I might refer to the width and height of an element collectively as its size.

---
# Observation 1

Say I have a child element and a parent element, and the child element is given a size of 5rem. If I don't specify any size for the parent element, it will take up as much space as it needs to in order to contain the child element, so 5rem in this case. If I specify the size of the parent element, it will be that size, even if it's smaller than the size of its child element.

When using CSS variables, you can specify a fallback value, like `var(--size, 0)`. By doing that, if `--size` isn't defined, the fallback value will be used, so 0 in this case. I ran into a slight problem with this due to my own convention. So what I like to do is define any CSS variables that I set as inline styles with an empty string... so if I'll be setting the variable `--size` as an inline style from my JavaScript, I still like to define it in my CSS file as `--size: ""`, so that way I can easily reference it in my stylesheet. The inline style for `--size` will take precedence over the same variable defined in the CSS, so the empty string doesn't do anything wrong. The problem I have come across is that if I use a fallback value for one of those variables and I don't define it in my inline styles, the fallback value won't be used. I read that the empty string would be considered an invalid value or something resulting in the fallback value being used, but that's not what I've experienced. I'm not sure what exactly happens in that case, but it's definitely not the fallback value being used and it has the same effects as me simply not specifying anything for that CSS property, so I think the empty string might just be whatever the default value is for that property.

---
