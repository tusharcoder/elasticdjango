# elasticdjango
#to set up the project
```bash
run virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
#to migrate
```bash
python manage.py makemigrations core
python manage.py migrate
```
#to run project
```bash
python manage.py runserver
```
