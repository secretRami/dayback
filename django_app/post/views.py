from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import ListAPIView

from post.models import Mood
from post.serializers import MoodSerializer


## 제네릭 뷰로 작성
# class mood_list(generics.ListAPIView):
#     queryset = Mood.objects.all()
#     serializer_class = MoodSerializer


## 그냥 작성
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def mood_list(request):
    if request.method == 'GET':
        mood = Mood.objects.all()
        print(mood)
        serializer = MoodSerializer(mood, many=True)
        print(serializer.data)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MoodSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def mood_detail(request, pk):
    try:
        mood = Mood.objects.get(pk=pk)
    except Mood.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MoodSerializer(mood)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MoodSerializer(mood, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        mood.delete()
        return HttpResponse(status=204)


