# Next Project

---

This file should describe the essential information about the project.

---

# Installation Guide for Next.js

---

[Installation Guide for Next.js](https://nextjs.org/docs/app/getting-started/installation)

- The documentation for this process is linked above.
- The section below will walk you through the manual installation process for Next.js.

---

1. The first step is to create a new folder for your project. This will be your project's root directory.

---

2. Create a README.md file in your root directoy that describes important stuff for your project like this file does.

---

3. The next step is to create a package.json file in your root directory like this...

``` json
{
  "name": "Next Project",
  "version": "1.0.0",
  "private": true,
  "license": "ISC",
  "main": "server.js",
  "type": "module",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  }
}
```

---

4. The next step is to run the following command in your terminal for your root directory.

``` shell
npm install next@latest react@latest react-dom@latest
```

- If the command was executed successfully...
  - You should see that both a file called package-lock.json and a folder called node_modules have been created in your root directory.
  - A folder called .next has also been created in your root directoy, but it's a hidden folder so you may not be able to see it.
  - Your package.json file should now look something like this...

``` json
{
  "name": "Next Project",
  "version": "1.0.0",
  "private": true,
  "license": "ISC",
  "main": "server.js",
  "type": "module",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "^15.0.3",
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  }
}
```

---

5. The next step is to create a .gitignore file in your root directory and reference both the node_modules folder and the .next folder like this...

``` gitignore
node_modules/
.next/
```

---

6. Create a folder called "app" in your root directory and then create two files inside of it with one called "layout" and one called "page" - use .jsx for JavaScript or .tsx for TypeScript.

---
