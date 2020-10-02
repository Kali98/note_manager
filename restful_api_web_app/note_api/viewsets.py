from rest_framework import viewsets
from . import models
from . import serializers


class NoteViewset(viewsets.ModelViewSet):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer

class NoteChangeViewset(viewsets.ModelViewSet):
    queryset = models.NoteChange.objects.all()
    serializer_class = serializers.NoteChangeSerializer
    http_method_names = ['get', 'head']