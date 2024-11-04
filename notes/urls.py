from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet

urlpatterns = [
    path('notes/user/<int:user_id>/', NoteViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-notes'),
    path('notes/user/<int:user_id>/<int:pk>/', NoteViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='note-detail'),
]
