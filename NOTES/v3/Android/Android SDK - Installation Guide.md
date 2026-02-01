
---

## **Installing `Android SDK`**

Make a directory called `android-sdk` (any name works).

---

On the following website, find the section named `Command line tools only` and then download the `SDK tools package` for `Windows`.

https://developer.android.com/studio

---

**Snapshot**
- `commandlinetools-win-14742923_latest.zip`
	- `cmdline-tools`

Extract `commandlinetools-win-14742923_latest.zip`.
Move `cmdline-tools` into `android-sdk`.
Delete `commandlinetools-win-14742923_latest.zip`

---

Create these `Environment Variables`

| Name           | Value                 |
| -------------- | --------------------- |
| `ANDROID_HOME` | path to `android-sdk` |
| `ANDROID_ROOT` | path to `android-sdk` |

---

`CWD` = path to `android-sdk/cmdline-tools/latest/bin`

``` powershell
./sdkmanager --licenses
```

``` powershell
./sdkmanager --list
```

**Example**

``` powershell
./sdkmanager "build-tools;36.1.0" "platform-tools" "platforms;android-36.1"
```

---
