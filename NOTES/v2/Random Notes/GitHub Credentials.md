
---
# Overview / Scenario

Let's say you have a GitHub account with a repository. You clone the repository and do some work. You're ready to update the remote repository, so you commit your work and then try to push it, but there's a problem... you're not allowed to push to the remote repository because you're signed in with a different GitHub account. You didn't realize it at the time, but you've been signed in with the wrong GitHub account the whole time, so all the commits you made are now logged with the wrong GitHub account and you don't have the permission to push those commits.

---
# Summary / Issue

So, you're signed into the wrong GitHub account and you want to sign out of it so you can sign in with your other GitHub account.

---
# Windows Solution

I'm not sure if the order of these steps matters, but this method worked for me.
## Steps

1. Navigate to `Control Panel > User Accounts > Credential Manager`, browse through your `Windows Credentials`, and look for an entry for GitHub. You should be able to open it to see more information, including the username of the wrong GitHub account you're currently signed into. You should be able to see an option to remove the credential... do that.
2. Additionally, you need to go to your terminal and change your GitHub email by running the following command...

``` shell
git config user.email your_email
```

## Additional Information

You can check your name and email with the following commands...

``` shell
git config user.name
git config user.email
```

You can change your name and email with the following commands...

``` shell
git config user.name your_name
git config user.email your_email
```

---
