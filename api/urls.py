from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^goods/$', views.good_list),
    url(r'^goods/([a-zA-Z]+)$', views.good_detail),
    url(r'^requests/$', views.request_list),
    url(r'^requests/([0-9]+)$', views.request_detail),
    url(r'^requests/([0-9]+)/activate$', views.request_activate),
    url(r'^offers/$', views.offer_list),
    url(r'^offers/([0-9]+)$', views.offer_detail),
    url(r'^offers/([0-9]+)/activate$', views.offer_activate),
    url(r'^users/$', views.user_list),
    url(r'^users/([a-zA-Z0-9]+)$', views.user_detail),
    url(r'^login/$', views.login),
]

urlpatterns = format_suffix_patterns(urlpatterns)
