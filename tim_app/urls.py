from django.conf.urls import url

from . import views

app_name = 'tim_app'
urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^request$', views.request, name='request'),
    url(r'^offer$', views.offer, name='offer'),         
]
