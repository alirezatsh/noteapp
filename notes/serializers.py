from rest_framework import serializers
from .models import Notes

class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'user', 'title', 'date', 'description', 'color', 'tag', 'isFavorite', 'isTrash']
        extra_kwargs = {
            'user': {'read_only': True},  # فیلد user فقط خواندنی است
            'title': {'required': False},
            'date': {'required': False},
            'description': {'required': False},
            'color': {'required': False},
            'tag': {'required': False},
            'isFavorite': {'required': False},
            'isTrash': {'required': False},
        }

    def create(self, validated_data):
        # user را از داده‌های ورودی حذف کرده و از request دریافت می‌کنیم
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
