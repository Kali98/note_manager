from django.shortcuts import render
from . import serializers
from . import models
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def api_root(request):
    api_urls ={
        'Get All Notes':'api/note-list/',
        'Get Note By ID':'api/note-list/<str:pk>/',
        'Create Note':'api/note-create/',
        'Update/Delete Note By ID': 'api/note-modify/<str:pk>/',
        'Get Whole Note Change History' : 'api/notehistory-list/',
        'Get Note Change History by ID' : 'api/notehistory-list/<str:note_id>',
    }
    return Response(api_urls)
    
@api_view(['GET'])
def note_list(request):
    notes = models.Note.objects.all() 
    serializer = serializers.NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def note_by_ID(request,pk):
    try:
        note = models.Note.objects.get(id=pk)
        serializer = serializers.NoteSerializer(note, many=False)
        return Response(serializer.data)
    except:
        msg = {"Note with this ID does not exist"}
        return Response(msg, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def note_create(request):
    '''
    JSON Request Body Example:
        {
        "title": "New Note",
        "content": "This note was written by me"
        }
    '''  
    serializer = serializers.NoteSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    else:
        msg = {"Title or Content cannot be left empty"}
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.data, status=status.HTTP_201_CREATED)

class NoteModify(APIView):
  
    def get_object(self,pk):
        try:
            return models.Note.objects.get(pk=pk)
        except models.Note.objects.get(pk=pk).DoesNotExist:
            msg = {"Note with this ID does not exist"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,pk):
        note = self.get_object(pk)   
        serializer = serializers.NoteSerializer(note)
        return Response(serializer.data)

    def put(self,request,pk):
        note = self.get_object(pk)
        
        serializer = serializers.NoteSerializer(instance=note, data=request.data)
        if serializer.is_valid():
            self.log_modified_note(request,pk,"UPDATED")
            serializer.save()
        else:
            msg = {"Title or Content cannot be left empty"}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request,pk):
        note = self.get_object(pk)
        self.log_modified_note(request,pk,"DELETED")

        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def log_modified_note(self,request,pk,note_action):
        print(note_action)
        note = self.get_object(pk)
        new_note_change =models.NoteChange.objects.create(
            corre_note = pk,
            title = note.title,
            content = note.content,
            created_date = note.created_date,
            modified_date = note.modified_date,
            action = note_action,
            version = (models.NoteChange.objects.filter(corre_note=pk).count())+1
        )
        serializer = serializers.NoteChangeSerializer(data =new_note_change)
        if serializer.is_valid() :
            serializer.save()
        return Response(serializer.data)
        

@api_view(['GET'])
def note_history_list(request):
    note_changes = models.NoteChange.objects.all()
    serializer = serializers.NoteChangeSerializer(note_changes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def note_history_by_ID(request,note_id):
    
    
    note_changes = models.NoteChange.objects.filter(corre_note=note_id)
    if not note_changes:
        msg = {"Note History with this ID does not exist"}
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    else :
        serializer = serializers.NoteChangeSerializer(note_changes, many=True)
        return Response(serializer.data)
