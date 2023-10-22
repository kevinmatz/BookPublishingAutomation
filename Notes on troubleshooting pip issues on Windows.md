- On Windows with Python 3.12.0, I get errors when trying to run "python -m pip install openai":

```
Building wheels for collected packages: aiohttp, frozenlist, multidict, yarl
  Building wheel for aiohttp (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building wheel for aiohttp (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [94 lines of output]
...
error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

- Build tools have been installed...

```
C:\Users\kevin>cl --version
Microsoft (R) C/C++ Optimizing Compiler Version 19.12.25835 for x64
```

...but error persists

- seems to be an issue with "aiohttp" being unable to be built with Python 3.12.0, at least on Windows...
  - https://stackoverflow.com/questions/74550830/error-could-not-build-wheels-for-aiohttp-which-is-required-to-install-pyprojec
  
- Let's try with a previous Python version:

```
PS C:\GitRepos\BookPublishingAutomation> conda create --name BookPublishingAutomationEnv python=3.9

PS C:\GitRepos\BookPublishingAutomation> conda activate BookPublishingAutomationEnv

PS C:\GitRepos\BookPublishingAutomation> python -m pip install openai
```

- Same issue persists

- Other people reporting similar issue on forums
- Will just give up trying on Windows and will try on Linux, although on a fresh install of Linux Mint, conda would not install, sigh (spent 4+ hours troubleshooting and many other people had the same problems, with no clear resolution)

