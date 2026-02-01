
---

## **Git**

`Git` is a distributed version control system that stores the history of a project as a direct acyclic graph of commits.

---

## **Repository**

A `repository` is a database.

A repository contains objects, references, configuration, and state.

A repository is stored on disk as a folder called `.git`.

---

## **Objects**

An `object` is an immutable value that can be addressed by its hash.

There are four types of objects:

- `blob`
- `tree`
- `commit`
- `tag`

A `blob` is the content of a file.

A `tree` is a snapshot of a directory.

A tree contains a list of entries that each have a:
- mode
- name
- hash

A `commit` is a snapshot of the entire project.

---

## **Commits**

A `commit` is a snapshot of a project.

It contains the following:

- a reference to the root directory tree
- reference(s) to zero or more parent commits

- `tree <tree-id>`
- `parent <commit-id>`
- `author <name> <email> <timestamp> <timezone>`
- `committer <name> <email> <timestamp> <timezone>`

The first/initial/root commit in a repository will have zero parent commits.

A normal commit will have one parent commit.

A merge commit will have multiple parent commits.

---

## **Branches**

A `branch` is a reference to a commit.

It's literally a file:
- its entire content is a single commit hash
- it's stored somewhere like `.git/refs/heads`

---

## **Locations**

- working directory
- staging area
- repository

---

## **Orphans**

A commit that has no branches pointing to it is considered to be `orphaned`.

---
