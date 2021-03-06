from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.NoticiaView.as_view()),
    path("<str:pk>/", views.NoticiaView.as_view()),
    #url(r'autores/', views.AutorView.as_view()),
    path("autores/", views.AutorView.as_view()),
]

