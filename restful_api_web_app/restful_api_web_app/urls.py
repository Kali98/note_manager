"""restful_api_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import note_api.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api_root, name="api_root"),
    path('api/note-list/', views.note_list, name="note_list"),
    path('api/note-list/<str:pk>/', views.note_by_ID, name="note_by_id"),
    path('api/note-create/', views.note_create, name="note_create"),
    path('api/note-modify/<str:pk>/',views.NoteModify.as_view(), name="note_upd_del"),
    path('api/notehistory-list/', views.note_history_list, name="notehistory_list"),
    path('api/notehistory-list/<str:note_id>/', views.note_history_by_ID, name="notehistory_by_id"),

]
