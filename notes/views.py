from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Notes
from .serializers import NoteSerializers

class NoteViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request, user_id=None):
        if str(request.user.id) != str(user_id):
            return Response({"detail": "Unauthorized."}, status=status.HTTP_403_FORBIDDEN)

        notes = Notes.objects.filter(user_id=user_id)
        serializer = NoteSerializers(notes, many=True)
        return Response(serializer.data)

    def create(self, request, user_id=None):
        serializer = NoteSerializers(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()  # user به طور خودکار به کاربر فعلی نسبت داده می‌شود
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, user_id=None, pk=None):
        if str(request.user.id) != str(user_id):
            return Response({"detail": "Unauthorized."}, status=status.HTTP_403_FORBIDDEN)

        note = Notes.objects.filter(user_id=user_id, id=pk).first()
        if not note:
            return Response({"detail": "Note not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = NoteSerializers(note)
        return Response(serializer.data)

    def update(self, request, user_id=None, pk=None):
        if str(request.user.id) != str(user_id):
            return Response({"detail": "Unauthorized."}, status=status.HTTP_403_FORBIDDEN)

        note = Notes.objects.filter(user_id=user_id, id=pk).first()
        if not note:
            return Response({"detail": "Note not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = NoteSerializers(note, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, user_id=None, pk=None):
        if str(request.user.id) != str(user_id):
            return Response({"detail": "Unauthorized."}, status=status.HTTP_403_FORBIDDEN)

        note = Notes.objects.filter(user_id=user_id, id=pk).first()
        if not note:
            return Response({"detail": "Note not found."}, status=status.HTTP_404_NOT_FOUND)

        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
