# selfieless

1. Fork the repo(if you haven't already)   
2. Create a virtualenv   
3. `git clone <your forked repo url>`   
4. `cd selfieless`   
5. `git remote add upstream <original repo link>`   

The above has to be done only the first time. Whenever you are editing the files, follow the following steps first   


1. `git fetch upstream`   
> If there are no changes, then you are free to go. Otherwise   

2. `git checkout master`   
3. `git merge upstream/master`   
4. `git status`    
> If it says untracked files, do the following   
5. `git add .`   
6. `git commit -m "<some commit message>"`   
7. `git push origin master`   

Like this, you will not have any issue.

Also, if you have changed the code, make sure to create a Pull Request.