from django.urls import path
from .views import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('ChooseGameMode/', views.ChooseGameMode, name='ChooseGameMode'),
    path('ChoosePlayerName/', views.ChoosePlayerName, name = 'ChoosePlayerName'),
    path('CreateGame/', views.CreateGame, name='CreateGame')

]