from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.db import models
import random
import string

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
        #Redirect to ChooseMultiPlayerGame page
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
        RoomCode = ''.join(random.choice(Characters) for _ in range(5))
      if Visibility == False:
        RoomCode = request.POST.get('Room-Code')
      
      NewGame = models.Game(Type=GameType, MaxPlayers = PlayerNumber, Public = Visibility, Roomcode= RoomCode)

      NewGame.Save()
        

  
    return render(request, 'CreateGame.html')
    
     
