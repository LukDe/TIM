from django.contrib import admin
from .models import User, Request, Supply, Good

# Register your models here.
admin.site.register(User)
admin.site.register(Request)
admin.site.register(Supply)
admin.site.register(Good)
