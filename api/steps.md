virtualenv hire_api
source bin/activate
pip install -r requirements.txt
django-admin startproject api  

python manage.py runserver
python manage.py startapp HireApp
python manage.py makemigrations HireApp
python manage.py migrate HireApp
