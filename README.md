# `django channels on ec2`
`django channels`를 `ec2`에 올려 노티 기능을 만들어 보기 위한 프로젝트

# 프로젝트 셋팅
1. `mkdir django-channels-on-ec2`
2. `cd django-channels-on-ec2`
3. `git init`
4. `touch .gitignore` <https://www.gitignore.io/>에서 `git,linux,macos,python,django,pycharm+all` 검색후 복사      
        1. `.secrets` 추가
5. `pyenv virtualenv 3.6.5 ec2`
6. `pyenv local ec2`
7. `pip install django`
8. `django-admin startproject config`
9. `mv config app`
10. `pip freeze > requirements.txt`
11.`settings.py` 수정
    ```python
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ROOT_DIR = os.path.dirname(BASE_DIR)
    
    TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
    
    SECRETS_DIR = os.path.join(ROOT_DIR, '.secrets')
    SECRETS_BASE = os.path.join(SECRETS_DIR, 'base.json')
    
    secrets = json.loads(open(SECRETS_BASE, 'rt').read())
    
    SECRET_KEY = secrets['SECRET_KEY']
    
    ALLOWED_HOSTS = [
        '.amazonaws.com',
    ]
    ```
    
12. `git hub` 설정         
        1. `git hub` -> `new repository` -> `django-channels-on-ec2`        
        2. `git remote add origin git@github.com:himanmenGit/django-channels-on-ec2.git`        
        3. `git push -u origin master`
13. `git add -A && git commit -m 'first commit'`

# ec2 셋팅
1. `ec2 instance 생성`
2. `ubuntu 16.04` 선택
3. `t2.micro` 프리티어 선택
4. 다음,다음,다음 6단계 보안 그룹 구성
5. 새 보안 그룹 생성       
        1. 보안 그룹 이름 - `EC2 Security Group`
        2. 보안 그룹 설명 - `Ec2 Deploy Security Group`
        3. 소스 - `내 IP`, 설명 - `ssh`
        4. 규칙 추가 - `사용자 지정 TCP`, 포트 번호 `8000`, 소스 `내 IP`, 설명 `web`
6. 검토 및 시작 - 시작
7. 키페어를 저장 후 인스턴스 시작 (`permission` 에러 나면 `chmod 400 <key pair>.pem`)
8.  `'ssh -i <key path>ex)~/key.pem ubuntu@<ec2 ip4 퍼블릭 IP>',`
9. `YES` - `Welcome to Ubuntu 16.04`
10. `linux setting`     
        1. `sudo vi /etc/default/locale`
        2. `locale` 수정      
            ```
            LC_CTYPE="en_US.UTF-8"
            LC_ALL="en_US.UTF-8"
            LANG="en_US.UTF-8"
            ```
        3. 재 접속        
11. `linux update`      
        1. `sudo apt-get update`    
        2. `sudo apt-get dist upgrade` 마지막에 엔터       
        3. `sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev`        
12. `pyenv` 설치      
        1. `curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash`          
        2. `vi ~/.bash_profile`에 마지막 설정 복사      
        3. `source ~/.bash_profile`적용       
        4. `pyenv` 명령 확인              
    ```
    export PATH="/home/ubuntu/.pyenv/bin:$PATH"            
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    ``` 
                
13. `git`설치      
        1. `sudo apt-get install libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev`      
        2. `git` 확인
        
14. `srv`폴더 유저 변경       
        1. `sudo chown -R ubuntu:ubuntu /srv/`
15. 프로젝트 `clone` 및 `pyenv` 설정   
        1. `git clone <django-channels-on-ec2 repository url>.git`      
        2. `cd django-channels-on-ec2`      
        3. `pyenv install 3.6.5`        
        4. `pyenv virtualenv 3.6.5 ec2`     
        5. `pyenv local ec2`        
16. `.secrets`폴더 업로드        
        1. `scp -ri <key_path>.pem .secrets ubuntu@<public ipv4>:/srv/django-channels-on-ec2/` 
17. `runserver`     
        1. `pip install -r requirements.txt`        
        2. `./manage.py runserver 0:8000`       
18. 브라우저 확인     
        1. 브라우저에 `<public dns주소>:8000`으로 접속 
        2. 로켓 발싸!