
---

## **Install Dependency with NPM**

``` powershell
npm install react-native-keyboard-controller
```

---

## **Configure Android Manifest**

You need to make `android:windowSoftInputMode` = `adjustResize`.

My original idea, before learning about this library, was to use `adjustNothing` because I don't want the keyboard to have any effect on the window, like `adjustResize` or `adjustPan` do, but apparently `adjustResize` is required for this library in order to report accurate data about the keyboard, and the library will override the standard behavior of `adjustResize` making it act like `adjustNothing`. I haven't tested this, so I hope it does.

It should look something like this.

``` xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
  <application>
    <activity
      android:windowSoftInputMode="adjustResize"
    >
    </activity>
  </application>
</manifest>
```

So it turns out the "use `adjustResize` so the library works and then let the library override that behavior" thing was bullshit. Use `adjustNothing` like a sensible person.

---

## **`useReanimatedKeyboardAnimation()`**

This hook will return an object of the type `ReanimatedContext`, which looks like this...

``` ts
type ReanimatedContext = {
	height: SharedValue<number>
	progress: SharedValue<number>
}
```

The value of `height` will be a number that ranges from `0` (when the keyboard is hidden) to `x` (when the keyboard is visible), where `x` represents the height of the keyboard.

The value of `progress` will be a number that ranges from `0` (when the keyboard is hidden) to `1` (when the keyboard is visible).

---
