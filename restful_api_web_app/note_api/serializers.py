from rest_framework import serializers
from .models import Note
from .models import NoteChange

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields ="__all__"

class NoteChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteChange
        fields= "__all__"