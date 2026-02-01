
---

## **Install Dependency with NPM**

``` powershell
npm install react-native-reanimated
```

---

## **Configure Babel**

You need to to add the following item to the array of plugins in `babel.config.js`

``` js
"react-native-reanimated/plugin"
```

It should look something like this.

``` js
module.exports = {
  plugins: ["react-native-reanimated/plugin"]
}
```

I'm not sure what this does exactly, but that's what AI said to do, and I remember doing this in an older project of mine as well, so I do believe there's a good reason for doing this.

---

## **Install React Native Worklets**

When I tried to build my app via `npm run android`, I got an error about `react-native-reanimated` telling me to install `react-native-worklets`.

``` powershell
npm install react-native-worklets
```

---
