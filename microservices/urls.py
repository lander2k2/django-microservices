from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',          views.home,     name='home'),
    url(r'^services/$', views.services, name='services'),
]

