from rest_framework import serializers

from post.models import Mood


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ('id', 'created_date', 'mood_chk', 'mood_comment')
