
---

# Disclaimers

This process was successfully performed on Windows.

---

# Step 1: Install Node.js

- Install the latest version of Node.js
- You can download Node.js from their website.
	- [Node.js Official Website](https://nodejs.org/)

---

# Step 2: Verify Node.js

- You can check the version of Node.js with either of the following commands.

```
node --version
node -v
```

---

# Step 2: Verify Corepack

- With Node.js installed, you should already have Corepack.
- You can check the version of Corepack with either of the following commands:

```
corepack --version
corepack -v
```

---

# Step 3: Verify NPM

- With Node.js installed, you should already have NPM.
- You can check the version of NPM with either of the following commands:

```
npm --version
npm -v
```

- If you get an error about not being able to run the script, you can run the following command in PowerShell to fix it:

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

- You should now be able to check the version of NPM as well as use NPM.

---

# Step 4: Configure PNPM

- Run the following commands:

```
corepack enable
corepack prepare pnpm@latest --activate
```

- If you get an error about an invalid key id/signature or whatever, ensure you have the latest version of Node.js installed, which will also give you the latest versions of NPM and Corepack.

---

# Step 5: Verify PNPM

- You can check the version of PNPM with the following commands:

```
pnpm --version
pnpm -v
```

- If you get an error about not being able to run the script, you can run the following command in PowerShell to fix it:

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

- You should now be able to check the version of PNPM as well as use PNPM.

---
