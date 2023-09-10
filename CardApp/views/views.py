from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.db import models
import random
import string
from CardApp.models import Game

def home(request):
    return render(request, 'home.html')

def ChooseGameMode(request):
    return render(request, 'ChooseGameMode.html')

def ChoosePlayerName(request):
     if request.method == 'POST':
        #Read Player Name Input
        Player_Name = request.POST.get('Player Name', '')
        #Create A Session var with value: Player_Name
        request.session['Player Name'] = Player_Name
        print(request.session.get('Player Name'))
        #Redirect to ChooseMultiPlayerGame page needs to redirect to game select which redirects to game page
        return redirect(reverse('ChooseMultiPlayerGame'))
     else:
        return render(request, 'ChoosePlayerName.html')
     
def CreateGame(request):

    if request.method == 'POST':
      GameType=request.POST.get('Game')
      PlayerNumber = request.POST.get('Game')
      Visibility = request.POST.get('Visibility')
      if Visibility == True:
        #generate random room code
        Characters = string.ascii_letters + string.digits
        Roomcode = ''.join(random.choice(Characters) for _ in range(5))
      if Visibility == False:
        Roomcode = request.POST.get('Room-Code')

      
      NewGame = Game(Type=GameType, MaxPlayers = PlayerNumber, Public = Visibility, Roomcode= Roomcode,)
      NewGame.Save()
      return redirect(request, 'ChoosePlayerName')
  
    else:   
      return render(request, 'CreateGame.html')
    
     
