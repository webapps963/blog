from django.conf.urls import url
from order import views

urlpatterns = [
    url(r'^$', views.order, name='order'),
    url(r'^orderCreate/$', views.orderCreate, name='orderCreate'),
]