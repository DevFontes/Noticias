from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r"^$", views.AutorView.as_view()),
    path("<str:pk>/", views.NoticiaView.as_view()),
    path("<str:autor_id>/", views.AutorView.as_view()),
]
