
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home, name="home"),
    path(r'getUrl', views.getUrl, name="getUrl"),
    path(r'download', views.download, name="download")
]