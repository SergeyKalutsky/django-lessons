from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('score', views.score, name='score'),
    path('daytime', views.daytime, name='daytime'),
    path('score_and_time', views.score_and_time, name='score_and_time'),
    path('lootbox', views.lootbox, name='lootbox'),
]