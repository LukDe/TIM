from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^goods/$', views.good_list),
    url(r'^goods/([a-zA-Z]+)$', views.good_detail),
    url(r'^requests/$', views.request_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
