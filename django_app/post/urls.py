from django.conf.urls import url

from . import views

urlpatterns = [
    ##제네릭 뷰를 이용한 코드용 url
    url(r'^post/$', views.Mood_list.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$', views.Mood_detail.as_view()),
]
