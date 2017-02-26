"""movie_knight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from mvindex.views import index, Create_New_User, Login, Create_View, Quiz, Predictor

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^new-user/$', Create_View, name='new-user'),
    url(r'^create/$', Create_New_User, name='create-user'),
    url(r'^login/$', Login, name='login'),
    url(r'^quiz/$', Quiz, name='quiz'),
    url(r'^results/$', Predictor, name='predictor'),
]
