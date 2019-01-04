# `django channels on ec2`
`django channels`를 `ec2`에 올려 노티 기능을 만들어 보기 위한 프로젝트

# 프로젝트 셋팅
1. `mkdir django-channels-on-ec2`
2. `cd django-channels-on-ec2`
3. `git init`
4. `touch .gitignore` <https://www.gitignore.io/>에서 `git,linux,macos,python,django,pycharm+all` 검색후 복사
5. `pyenv virtualenv 3.6.5 ec2`
6. `pyenv local ec2`
7. `pip install django`
8. `django-admin startproject config`
9. `mv config app`
10. `pip freeze > requirements.txt`
11. `git add -A && git commit -m 'first commit'` 

# git hub
1. `git hub` -> `new repository` -> `django-channels-on-ec2`
2. `git remote add origin git@github.com:himanmenGit/django-channels-on-ec2.git`
3. `git push -u origin master`

# ec2 셋팅

