from rest_framework import viewsets

from post.models import Mood
from post.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Mood.objects.all()
    serializer_class = PostSerializer
