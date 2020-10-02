from django.shortcuts import render
from django.http import JsonResponse
from . import serializers
from . import models
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request):
    api_urls ={
        'Get All Notes':'api/note-list/',
        'Get Note By ID':'api/note-list/<str:pk>/',
        'Create Note':'api/note-create/',
        'Update Note By ID': 'api/note-update/<str:pk>/',
        'Delete Note By ID': 'api/note-delete/<str:pk>/',
        'Get Whole Note Change History' : 'api/notechange-list/',
        'Get Note Change History by ID' : 'api/notechange-list/<str:ID>',
    }
    return Response(api_urls)
    
@api_view(['GET'])
def note_list(request):
    notes = models.Note.objects.all()
    serializer = serializers.NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def note_by_ID(request,pk):
    notes = models.Note.objects.get(id=pk)
    serializer = serializers.NoteSerializer(notes, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def note_create(request):
    serializer = serializers.NoteSerializer(data=request.data)
    return Response(serializer.data)

