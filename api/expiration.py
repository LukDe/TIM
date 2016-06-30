from tim_app.models import Request
from dateutil.parser import *
from datetime import datetime, timedelta
from django.utils import timezone

def check_if_expired():
  requests = Request.objects.all().filter(active = True)
  for r in requests:
    if parse(str(r.creationDate)) > timezone.now() + timedelta(days = r.priority):
      print (r.goodName)
      r.active = False
      r.save()