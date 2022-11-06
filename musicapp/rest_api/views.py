from django.shortcuts import render
from .models import Artiste
from .serializers import ArtisteSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Song
from .serializers import SongSerializer


# Create your views here.
@csrf_exempt

def ArtisteView(request):

    if request.method == 'GET':
        posts = Artiste.objects.all() #querySet
        serializer = ArtisteSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe= False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArtisteSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

        


@csrf_exempt
def SongView(request):

    if request.method == 'GET':
        posts = Song.objects.all() #querySet
        serializer = SongSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe= False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SongSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
