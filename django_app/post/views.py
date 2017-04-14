import django_filters
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer

User = get_user_model()


class PostFilter(django_filters.rest_framework.FilterSet):
    created_date_year = django_filters.NumberFilter(name='created_date', lookup_expr='year')
    created_date_month = django_filters.NumberFilter(name='created_date', lookup_expr='month')
    created_date_day = django_filters.NumberFilter(name='created_date', lookup_expr='day')

    class Meta:
        model = Post
        fields = ('created_date_year', 'created_date_month', 'created_date_day')


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    filter_class = PostFilter
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
