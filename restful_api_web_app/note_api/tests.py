import json

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.test import RequestFactory
from .models import Note
from .models import NoteChange

from.serializers import NoteSerializer
from.serializers import NoteChangeSerializer

class NoteTestCase(APITestCase):

    def test_get_note_list(self):
        response = self.client.get("/api/note-list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_note_by_id(self):
        response = self.client.get("/api/note-list/", kwargs={"pk": 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_note(self):
        data ={"title":"My New Note test", "content":"I have created this new note with utter most passion"}
        response = self.client.post("/api/note-create/",data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_invalid_note(self):
        data ={"title":"", "content":"I have created this new note with utter most passion"}
        response = self.client.post("/api/note-create/",data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_notehistory_list(self):
        response = self.client.get("/api/notehistory-list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_notehistory_by_id(self):
        response = self.client.get("/api/notehistory-list/", kwargs={"pk": 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    