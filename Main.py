import time

from random import randint

for i in range(1,100):

    print('  ')

space='  '

for i in range(1,1000):

    count=randint(1,99)

    while(count>0):

        space+=' '

        count-=1

    if(i%10==0):

         print(space+ 'Happy Birthday!')

    elif(i%9==0):

         print(space+'🎊Happy Birthday Chirag tankan')

    elif(i%8==0):

         print(space+'🎂')

    elif(i%7==0):

         print(space+'🥞Happy Birthday Chirag tankan')

    elif(i%6==0):

         print(space+'Happy Birthday Chirag tankan 🍩')

    elif(i%5==0):

         print(space+'🍰')

    elif(i%4==0):

         print(space+'🍫')

    elif(i%3==0):

         print(space+'🥧')

    elif(i%2==0):

         print(space+'Happy Birthday Chirag tankan🧁')

    elif(i%1==0):

         print(space+'🍨')

    space='  '

    time.sleep(0.2)
# Byte-compiled / optimized / DLL files
__pycache__/

*$py.class

# C extensions
*.so

#  / packaging
.Python
/


# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy


#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
) you can uncomment the following to ignore the entire idea folder.

