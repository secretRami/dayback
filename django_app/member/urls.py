from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# Router to gather both user and group lists.
# 사용자, 그룹 목록을 처리하기 위한 라우터.
router.register(r'user', views.UserViewSet)
router.register(r'group', views.GroupViewSet)

urlpatterns = [
    url('', include(router.urls)),
    # URL for authentication
    # 인증처리를 위한 URL
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
