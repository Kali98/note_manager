from note_api.viewsets import NoteViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('note', NoteViewset)