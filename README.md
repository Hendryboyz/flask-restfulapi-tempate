## Require Scripts

### Install Development Environment
``` sh
# Installtion
py -m venv venv
pip install -r requirements.txt

# Upgrade Dependency
pip freeze > requirements.txt
```

### Run in Local Machine
``` sh
#Local development for Linux
export FLASK_APP=flaskr
export FLASK_ENV=development

flask run
```

``` powershell
# Local development for Windows powershell
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"

flask run
```