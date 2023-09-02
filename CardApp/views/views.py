from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

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
     
def ChooseMultiPlayerGame(request):
    return render(request, 'ChooseMultiPlayerGame.html')
    
     
