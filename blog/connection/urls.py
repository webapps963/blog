from django.conf.urls import url
from connection import views

urlpatterns = [
    url(r'^$', views.connection, name='connection'),
]