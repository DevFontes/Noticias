from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.NoticiaView.as_view()),
    path("<str:pk>/", views.NoticiaView.as_view()),
    #url(r'autores/', views.AutorView.as_view()),
    path("autores/", views.AutorView.as_view()),
]


# boas praticas de commit

# commits tem um TIPO e a DESCRIÃO, tbm podem ter outras coisas

# basicamente: (À GROSSO MODO)

    # feat: mensagem -> para adições de código e funcionalidades. (feat means feature)
    # fix: mensagem -> correção de bugs
    # chore: mensagem -> atividades que não alteram código fonte da aplicação.

    # ... etc