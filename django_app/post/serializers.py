from rest_framework import serializers

from post.models import Mood, MOOD_CHOICE


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ('id', 'mood_chk', 'mood_comment')
