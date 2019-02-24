# selfieless

1. Fork the repo(if you haven't already)   
2. Create a virtualenv   
> virtualenv -p python3 env      
3. `git clone <your forked repo url>`   
4. `cd selfieless`   
5. `git remote add upstream <original repo link>`   
6. `pip3 install -r requirements.txt `   
> Make sure you are in your virtual environment.   


The above has to be done only the first time. Whenever you are editing the files, follow the following steps first   

1. `source env/bin/activate`   
2. `git fetch upstream`   
> If there are no changes, then you are free to go. Otherwise   

3. `git checkout master`   
4. `git merge upstream/master`   
5. `git status`    
> If it says untracked files, do the following   
6. `git add .`   
7. `git commit -m "<some commit message>"`   
8. `git push origin master`   

If you follow this, you will not have any issue.

Also, if you have changed the code, make sure to create a Pull Request.
