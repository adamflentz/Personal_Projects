# kitchenpantry/urls.py
from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.home.as_view()),
    url(r'^profile/$', views.profile.as_view()),
    url(r'^recipequery/$', views.recipequery.as_view()),
    url(r'^recipecards/$', views.recipecards.as_view(), name="recipes"),
]