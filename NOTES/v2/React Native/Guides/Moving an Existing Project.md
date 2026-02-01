
---

## **Notes**

I moved my project (the root folder) and tried to run my app via `npm run android`. I got an error and in the message it referenced the old location of my project. I followed these steps and my problem was solved.

---

## **Relevant Project Structure**

I don't mention `package.json`, but it's necessary when you run `npm install`.

- `root`
	- `android`
	- `node_modules`
	- `package.json`
	- `package-lock.json`

---

## **Stop Everything**

Any terminals running your app... etc.

---

## **Remove Android Stuff**

Ensure your CWD is `root/android`.

``` powershell
Remove-Item -Recurse -Force .gradle -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force build -ErrorAction SilentlyContinue
```

---

## **Remove Root Stuff**

Ensure your CWD is `root`.

``` powershell
Remove-Item -Recurse -Force node_modules -ErrorAction SilentlyContinue
Remove-Item package-lock.json -Force -ErrorAction SilentlyContinue
```

---

## **Install Dependencies**

**With NPM**

``` powershell
npm install
```

---

## **Reset Metro Cache**

Ensure your CWD is `root`.

``` powershell
npx react-native start --reset-cache
```

``` powershell
Ctrl + C
```

---

## **Clean Gradle**

Ensure your CWD is `root/android`.

``` powershell
./gradlew clean
```

---

## **Attempt**

Ensure your CWD is `root`.

``` powershell
npx react-native run-android
```

**My Alias (default)**

``` powershell
npm run android
```

---
