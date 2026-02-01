
---

# **Preparing to Create a New Project**

Install `Visual Studio Code` (`VS Code`)

https://code.visualstudio.com/

---

Install `Node.js` (`Node`)

https://nodejs.org/en/download

---

Install `Java`.
- React Native recommends JDK 17

https://www.oracle.com/java/technologies/downloads/

If you download the compressed archive rather than the installer.

Unzip the folder.

Set environment variable `JAVA_HOME` = `<path to folder>`

---

Install Android SDK

[[Android SDK]]

---

Install `Git` (optional)

https://git-scm.com/install/

---

# **Actually Creating the New Project**

Using a `Powershell` terminal in `Visual Studio Code`, change your current working directory to wherever you want to create your new project folder.

Let's say your current working directory is `C:\User\Projects`.

Think of a name for your project. I would use kebab-case for the name.

Let's say you want to create a new project named `lynx`.

Run the following command.

``` powershell
npx @react-native-community/cli@latest init lynx
```

You should now see a folder named `lynx` in your current working directory.

---

# **Configuring Your Package Manager**

By default, the new project uses `NPM`.

I've been using `PNPM` as my standard lately, but using it in a `React Native` project was giving me some errors in the `node_modules` or `android` folders.

I recommend using `NPM` in `React Native` projects.

---

## **Using NPM**

Check which version of `NPM` is installed on your device.

``` powershell
npm --version
```

Let's say your `NPM` version is `11.5.2`.

Run the following command.

``` powershell
corepack use npm@11.5.2
```

This will set the `packageManager` field in your `package.json` file.

You may or may not need to run the following command.

``` powershell
npm install
```

---

## **Using PNPM**

Since `NPM` is used by default, you need to delete both the `node_modules` folder and `package-lock.json` file from your project.

Check which version of `NPM` is installed on your device.

``` powershell
npm --version
```

Let's say your `PNPM` version is `10.24.0`.

Run the following command.

``` powershell
corepack use pnpm@10.24.0
```

This will set the `packageManager` field in your `package.json` file.

You may or may not need to run the following command.

``` powershell
pnpm install
```

---

## **Note**

I was going to say that having the `packageManager` field set in `package.json` is optional, which is true, but the good thing about having it is that it will prevent you from using other package managers to install stuff. For example, if `packageManager` is set to `npm`, then attempting to run something like `pnpm install ...` will be rejected.

---

# **Setting Up a Wireless Android Connection**

I believe the android device must be `Android 11+` in order to do this with no cables involved.

---

Use your computer.

Ensure that `Environment Variables > User Variables > Path` includes the path to `platform-tools` from your `android-sdk`. My path is `C:\Jack\Software\android-sdk\platform-tools`.

You can run the following command to check.

``` powershell
adb --version
```

---

Use your phone.

Open to `Settings > Developer Options`.

If you don't see `Developer Options`, there's a button on your phone that you have to click 7 times in order to have it show up. I forgot what it is, so figure it out.

Find and then click on `Wireless debugging`.

Enable wireless debugging and then click on `Pair device with pairing code`.

You should see two variables: `Wi-Fi pairing code` and `IP address & Port`.

Let's say your values are:
`IP address & Port` = 192.168.0.1:12345
`Wi-Fi pairing code` = 123456

Remember those values.

---

Use your computer.

Using the value of `IP address & Port`, run the following command

``` powershell
adb pair 192.168.0.1:12345
```

You'll be prompted to enter the `Wi-Fi pairing code`. Do that.

Your device should now be linked.

---

Use your phone.

On the wireless debugging screen, you should see a value named `IP address & Port`. As opposed to the value of `IP address & Port` you see when you click on `Pair device with pairing code`, the IP address is the same but the port is different.

Let's say the value of `IP address & Port` is `192.168.0.1:67890`.

---

Use your computer.

Run the following command.

``` powershell
adb connect 192.168.0.1:67890
```

Your device should now be connected.

You can check by running the following command.

``` powershell
adb devices
```

You should see your device listed.

---

I had trouble building my app with `pnpm android` / `react-native run-android`. I was using `JDK 25`. I switched from `JDK 25` to `JDK 17`, meaning I changed the value of my environment variable `JAVA_HOME` from the path of my `JDK 25` folder to the path of my `JDK 17` folder. Once I did that, my build was successful.

---

Ensure your current working directory is the root folder of your project.

Run the following command.

``` powershell
react-native run-android
```

---

If everything is successful, then once you start your app with `react-native start`, you should be able to open/launch the app on your android device and see any changes you make reflected live.

---

# **Expo Modules**

I ran `npx install-expo-modules@latest` and got an error.

I downgraded my version of `react-native` from `0.82.x` to `0.81.x`.

I ran `npx install-expo-modules@latest` again, but got a different error.

It seems the solution to that problem is to either use an even older version of `react-native` or manually configure `expo`. I don't want want to do either of those things.

---
