
---

I created a new `React Native` project named `lynx` using the following command.

``` powershell
npx @react-native-community/cli@latest init lynx
```

The following dependencies were automatically included in `package.json`.

| Dependency                       | Version  |
| -------------------------------- | -------- |
| `react`                          | `19.1.1` |
| `react-native`                   | `0.82.1` |
| `react-native-safe-area-context` | `^5.5.2` |

When I run `pnpm android`, the build is successful.

---

I installed `react-native-track-player` using the following command.

``` powershell
pnpm add react-native-track-player
```

The following dependency was added to `package.json`

| Dependency                  | Version  |
| --------------------------- | -------- |
| `react-native-track-player` | `^4.1.2` |

When I run `pnpm android`, the build fails.

---

In all my attempts to solve this problem, the build has ultimately failed.

I've decided to avoid `react-native-track-player` for the foreseeable future.

---

I removed `react-native-track-player` using the following command.

```
pnpm remove react-native-track-player
```

The following dependency was removed from `package.json`

| Dependency                  | Version  |
| --------------------------- | -------- |
| `react-native-track-player` | `^4.1.2` |

When I run `pnpm android`, the build is successful.

---
