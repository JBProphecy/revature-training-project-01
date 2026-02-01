
---
# Instructions

1. Create a folder on your device where you want to initialize your git repository.
2. From a terminal, navigate to your new folder.
3. Run `git init` to initialize it as a git repository.

``` shell
git init
```

---

4. Create a remote repository on GitHub.
5. Copy the URL from the remote repository and run `git remote add origin <URL>`.

``` shell
git remote add origin <URL>
```

---

- If you already have at least one commit, you can skip this step.

6. Make an initial commit by running `git add .` and `git commit -m "<message>"`.
	- The message can be whatever you want it to be.
	- There may need to be at least one file for the commit to work.

``` shell
git add .
git commit -m "<message>"
```

---

7. Run `git push -u origin <branch>`.
	- The branch is most likely called `master` or `main`.
	- You can check which branch is is by running `git branch`.

``` shell
git push -u origin <branch>
```

---
