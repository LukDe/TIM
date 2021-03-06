"""TIM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponseRedirect


from tim_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Redirect user to /tim if no path is specified.
    url(r'^$', lambda r: HttpResponseRedirect('tim/ranking')),
    # Admin page.
    url(r'^admin/', admin.site.urls),
    # Initial app page.
    url(r'^tim/', include('tim_app.urls')),
    # Our REST api
    url(r'^api/', include('api.urls'))
]

# Icon folder
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
