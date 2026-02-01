
---

When you do a merge, you'll be merging changes from the selected branch into the current branch. For example, if you have two branches called `master` and `feature` and you want to merge the changes from `feature` into `master`, you need to be on the `master` branch and then merge the `feature` branch into it, which you can do with the following commands:

- `git branch` (to determine which branch is currently active)
- `git checkout master` (to change the current branch to `master` if needed)
- `get merge feature` (to merge the changes from `feature` into the current branch)

Once you successfully run those commands, you can delete the `feature` branch if you want.

- `git branch -d feature` (to delete the `featue` branch)

---
