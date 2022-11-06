from rest_framework import serializers
from .models import Artiste
from .models import Song

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['first_name','last_name','age']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['Artiste_id', 'title','date_released','likes']



  