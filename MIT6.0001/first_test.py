print("this is my first try on git, as well as my first python code")
print("second version test")

# git push on terminal works fine, while none of commands doesn't work on VS code (including push/pull/commit), unless I do this;
# 1. start ssh-agent on bash
# 2. code on bash to open VS code
# 3. commit on VS code
# Furthermore, it requires me to input SSH private key password every time.

# So far, I found two work two workarounds.
# a. using https instead of ssh. (git remote set-url origin https://github.com/USERNAME/REPOSITORY.git)