
---

```
git reset --soft <commit_hash>
```

If `HEAD` is attached:
- the current branch will be updated to reference the specified commit.
	- `HEAD` will still reference the current branch, which now references the specified commit
- the `index / staging area` will not change
- the `working directory` will not change

---

```
git reset --mixed <commit_hash>
```

If `HEAD` is attached:
- the current branch will be updated to reference the specified commit.
	- `HEAD` will still reference the current branch, which now references the specified commit
- the `index / staging area` will be updated to match the tree of the specified commit
- the `working directory` will not change

---

```
git reset --hard <commit_hash>
```

If `HEAD` is attached:
- `HEAD` references the current branch, which references the current commit
- the current branch will be updated to reference the specified commit.
- `HEAD` still references the current branch, which now references the specified commit
- the `index / staging area` will be updated to match the tree of the specified commit
- the `working directory` will be updated to match the tree of the specified commit

---
