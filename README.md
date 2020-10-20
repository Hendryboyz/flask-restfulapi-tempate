## Require Scripts

``` shell
# Installtion
py -m venv venv
pip install -r requirements.txt

# Upgrade Dependency
pip freeze > requirements.txt

# Local development
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```