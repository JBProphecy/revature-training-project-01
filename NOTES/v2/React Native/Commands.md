
---

Every since I installed `react-native-reanimated` in my project, it's been taking forever to build my app via `npm run android`, my alias for `npx react-native run-android`.

The following command will build my app, but detect the architecture of the currently connected device (my phone using `adb pair` and `adb connect`), and only do stuff with that architecture rather than all of them, which drastically speeds up the build-time.

``` powershell
npx react-native run-android --active-arch-only
```

---
