from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^about/$', views.about, name='about'),
    url(r'^mainCreate/$', views.mainCreate, name='mainCreate'),
    url(r'^mainRead/(?P<mainId>[0-9]+)/$', views.mainRead, name='mainRead'),
    url(r'^mainUpdate/(?P<mainId>[0-9]+)/$', views.mainUpdate, name='mainUpdate'),
]