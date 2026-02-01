
---

I can have a component that its width and height set to 100% so that it takes up the full space of its container. If I need to use pixel values in my CSS, I can get the dimensions of that component and set them as CSS variables, where I can use them for all the child elements.

I can have a component where I set its width and height as hard values in the CSS.
- This does not allow for customizable sizes from the JS.

I can have a component where I set its dimensions as percentage values in the CSS.
- This alone does not work well for calculating the dimensions of child elements.
- I could get the hard values of the dimensions in JS and pass them as CSS variables.

I can have a component where I set its width and height as variables through props.
- Similar to the method above, except

---
# Issue 1

**Description:** I want my button to have a width based on its content. The way I've made my button is by having a relative element with absolute elements nested inside of it as layers. Since the content I want my width to be based on is an absolute element, I can't do that.

**Solution:** I made the element layer with the content a relative element. Since there's only one element in the layer stack that's relative, the positions still work correctly. So the layers (absolute with one relative) have a width and height of a 100% and their container has a max-width of max-content. I used max-width so the button can still shrink if needed. Essentially, the main relative element's width is being set based on the content of the one relative element nested inside of it, and the rest of the absolute elements nested inside of it are being determined based on that main element.

---
# Issue 2

**Description:** I want to be able to pass colors into my button to make it customizable in the best way, but I'm using `rgba` and the `a` part of that (opacity) is being determined from a CSS variable. I can't just pass the `rgb` string as a prop because it would be missing the opacity. I could pass each of the red, green, and blue values as separate props... each being set as a CSS variable that I could then use to build the `rgba` string, but I feel like that's way too much. There has to be a better way.

**Thoughts:** I'm thinking about not using `rgba` and instead apply the opacity another way. I've also bee thinking about not using opacity at all and instead just changing the color values for light and dark. I think the best option is the first option though. I'll try it when I make the fancy input component.

**Current Approach:** I stopped using `rgba` and I'm using opacity as a separate variable. Instead of transitioning the background color, I transition the opacity. I'm now able to pass colors as props and I've done so in the fancy module I created.

---
## Issue 3

**Description:** Currently, I'm setting the height of my input or button as a prop and without it it has a default value. For the input, the width is 100%, but for the button, the width is max-content. Given that there are multiple ways to size a component scenarios where I may want to use one method over another with the same component, I need to figure out a way to choose which method I want to use so I can do that without having to create multiple components.

**Sizing Types...**
- I could set the dimension to 100%.
- I could set the dimension to a certain value.
- I could set the dimension to be based on its content.

**Thoughts**
- For a list of buttons, I would definitely want to set the height and I could set the width to 100%. or have it based on its content.
- If I want two or three buttons next to each other, I would still set the height, but the width should probably be based on its content. If I want them to have equal sizes, I could use a grid and evenly distribute the cells, and then have each button set to 100% width.

**Thoughts**
- What if I want to have a header on my page, and then have a square button in the top-right corner at the end of the header? Instead of fiddling around with the props of the button to get the correct size, I should determine that in the layout. I could just make a div, set it to 100% height and aspect-ratio of 1, and then have the button dimensions set to 100%.
- Let's say I want to have a line of them up at the top, with each one having a width based on its content. I wouldn't need a container to do that. I could have the height for each button set to 100% and then have the content be max-content.
- I think I should have the button dimensions set to 100%. If I want the button to have a content-based width, I could set the width of its parent element to max-content. For the input elements...

**Thoughts**
- I can think of it like this... for whatever component I make, I can have the dimensions set to 100%, so it will always try to take up the full size of it's container. If I want to determine the size of it, I can wrap it in a div container and I can set the dimensions of that container to whatever values, including max-content. The only downside to this approach I can see is that determining the sizes like that requires that extra element. That's why I cut off the last thought about the input elements - if I have say 10 input elements that would all be in the form listed out, I would definitely want them to have a fixed size, like 60px. With the approach I described above, I would need to wrap each of my input elements in a div container set to a height of 60px. In my current approach, I can just set the height of the input element through a prop. I think the best of both worlds would be to have the dimensions set to 100% by default, but then have the optional ability to set the width or height or both to certain values.

**Issue**
- I just tried out that approach and it works great. I don't even need to set the wrapper element to have a dimension of max-content, just putting the div there does it all. The only problem I have right now is that without defining a height, my font-size isn't being calculated correctly, since it's being calculated with the value of the height. I just did some research and it turns out that you can't define font-size based on the height of its parent let alone anything else. Without having a pixel value to work with in the CSS, I would have to set the font size in JavaScript. That said, I should define a height when I need to calculate a font-size based on it.

**Thoughts**
- I definitely want to keep the dimensions set to 100% with the ability to set those values manually. It works great, with the only real issue being the font-size thing, which I can easily avoid by passing a value for the height. The wrapper thing works great too.

**Issue**
- I can avoid having to use a wrapper and be able to set max-content as a prop, but to do so, I have to change the type from a number to a string. This means that when I set the values as well, I have to pass say "500px" instead of just 500. With that, I wouldn't be able to work with the values in JavaScript without first parsing the value and turning it into a number. However, by passing a string value, I can easily pass the "max-content" or "500px" or even use the other methods like "10rem" and whatever else. With a number, I would need to convert that value into a string using "px" or "rem" and so on. I'm not really sure what approach I want to use, but honestly, I think the string method might be better. I could easily pass "0px" as a value as well. Right now, I'm having to check if the value is not undefined, because if I pass 0, that's a non-truthy value. A string of "0px" is truthy though.

**Final Thoughts**
- Okay, I just switch all the button props I could to string and it works really well. I was able to eliminate some code and completely take out the toPixelString function, and now I can pass the pixel values as strings as well as other values like %, rem, em, max-content, etc. I can pass any value that CSS would accept. Also, for the button component, I don't even need to work with styles in JavaScript, so there's no downside to doing it this way. Now, since I can pass a width of max-content, I don't even need the simple wrapper div, so my code should look really clean. I think I'll stick with this approach until I find a reason not to.

---
