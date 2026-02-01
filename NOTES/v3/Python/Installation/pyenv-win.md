
---

## **Installing `pyenv-win`**

The original installation process can be accessed through this link.
https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#pyenv-win-zip

You can download `pyenv-win-master.zip` with this link.
https://github.com/pyenv-win/pyenv-win/archive/master.zip

---

**Snapshot**
- `pyenv-win-master.zip`
	- `pyenv-win-master`

Extract `pyenv-win-master.zip`.
Delete `pyenv-win-master.zip`.

---

**Snapshot**
- `pyenv-win-master`
	- `...`
	- `pyenv-win`

The only thing you need from `pyenv-win-master` is `pyenv-win`.
Move `pyenv-win`.
Delete `pyenv-win-master`.

---

**Snapshot**
- `pyenv-win`
	- `bin`
	- `libexec`
	- `.versions_cache.xml`
	- `__init__.py`
	- `install-pyenv-win.ps1`

 Create these directories in `pyenv-win`.
- `shims`
- `versions`

**Snapshot**
- `pyenv-win`
	- `bin`
	- `libexec`
	- `shims`
	- `versions`
	- `.versions_cache.xml`
	- `__init__.py`
	- `install-pyenv-win.ps1`

---

Create these `Environment Variables`.

| Name         | Value               |
| ------------ | ------------------- |
| `PYENV`      | path to `pyenv-win` |
| `PYENV_HOME` | path to `pyenv-win` |
| `PYENV_ROOT` | path to `pyenv-win` |

Add these values to your `Path Environment Variable`.

| Value |
| - |
| path to `pyenv-win/bin` |
| path to `pyenv-win/shims` |

---
