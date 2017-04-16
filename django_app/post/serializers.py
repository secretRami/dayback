from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'id', 'created_date', 'mood_chk', 'mood_comment')
        ordering = ('created_date',)
