
---

## **HEAD**

`HEAD` is a special reference that:
- can reference a commit directly
- can reference a reference to a commit (branch, tag, ...)
- can be `symbolic / attached` or `detached`
- is `symbolic / attached` when when it references a local branch.
- is `detached` when it references a commit directly or a reference to a commit that is not a local branch

---

If you have a `detached HEAD`, make a commit, and then make `HEAD` reference another object without creating a reference to the commit that `HEAD` will no longer reference, that commit will become `orphaned`.

---
