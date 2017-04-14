from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'id', 'created_date', 'mood_chk', 'mood_comment')
        ordering = ('created_date',)

    def create(self, validated_data):
        return Post(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.created_date = validated_data.get('create_date', instance.created_date)
        instance.mood_chk = validated_data.get('mood_chk', instance.mood_chk)
        instance.mood_comment = validated_data.get('mood_comment', instance.mood_comment)
        return instance
