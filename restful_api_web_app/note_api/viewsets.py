from rest_framework import viewsets
from . import models
from . import serializers

class NoteViewset(viewsets.ModelViewSet):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer