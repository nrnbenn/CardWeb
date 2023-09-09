from django.db import models

# Create your models here.

class Game(models.Model):
    Type = None
    Players = []
    Maxplayers = 0
    Public = None
    Roomcode = ""
    
