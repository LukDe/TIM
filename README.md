Things to install:
- pip install django-cors-middleware (pip oder pip3)
- pip install djangorestframework
=======
## SMS:

To send a sms, on console:

 - python manage.py shell
 - `$ from sms.utils import send_sms_message`
 - `$ send_sms_message('+49<the_number>', 'Hello World')`
