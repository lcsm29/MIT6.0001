print("this is my first try on git, as well as my first python code")
print("second version test")

# git push on terminal works fine,
# but none of commands doesn't work on VS code (including push/pull/commit) and constantly gave me this error Git: git@github.com: Permission denied (publickey),
# unless I do this;
# 1. start ssh-agent on bash (on further testing, it seems like this step isn't neccessary)
# 2. code on bash to open VS code
# 3. commit on VS code
# Furthermore, it requires me to input SSH private key password every time.

# So far, I found two work two workarounds.
# a. using https instead of ssh. (git remote set-url origin https://github.com/USERNAME/REPOSITORY.git)
# 

# Disregard above. I think I found a solution.
# rename your private key as id.rsa (if it's not a rsa key, make one by using this ssh-keygen -t rsa -b 4096 –C "your_email@example.com")
# place the file on %USERPROFILE%/.ssh/id.rsa (Linux ~/.ssh/id_rsa)
# run below command on bash;
# git config --global credential.helper 'store --file %USERPROFILE%/.ssh/id.rsa'
# So far, it works as intended. No login. No nothing. It just works.

# Hopefully, Last test
# clone test