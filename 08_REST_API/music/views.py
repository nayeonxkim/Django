from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Music
from .serializers import MusicSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        data = Music.objects.all()
        serializer = MusicSerializer(data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.POST, many=True)

@api_view(['GET'])
def music_detail(request, music_pk):
    data = get_object_or_404(Music, pk=music_pk)
    serializer = MusicSerializer(data)
    return Response(serializer.data)