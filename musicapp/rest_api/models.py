from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    age = models.IntegerField()

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    date_released = models.DateField()
    likes = models.IntegerField()


class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=1000)

