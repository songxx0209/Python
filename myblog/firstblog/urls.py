from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^logins/', views.logins),
    url(r'^temp/', views.temp),
    url(r'^staff/', views.staff),
]