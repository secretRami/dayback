from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from post.models import Mood
from post.serializers import MoodSerializer


## 제네릭 뷰로 작성
class Mood_list(generics.ListAPIView):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer

class Mood_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer

