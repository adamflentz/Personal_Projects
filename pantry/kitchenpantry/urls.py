# kitchenpantry/urls.py
from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.home.as_view()),
]