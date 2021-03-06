from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1500)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    
class NoteChange(models.Model):
    corre_note = models.CharField(max_length=5)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1500)
    created_date = models.CharField(max_length=100)
    modified_date = models.DateTimeField(auto_now=True)
    action = models.CharField(max_length=10)
    version = models.CharField(max_length=5)
    


