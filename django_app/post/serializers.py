from rest_framework import serializers

from post.models import Mood


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ('author', 'id', 'created_date', 'mood_chk', 'mood_comment')
