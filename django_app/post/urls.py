from post.views import PostViewSet
from rest_framework import renderers

post = PostViewSet.as_view({
    'get': 'get_queryset',
    'put': 'perform_update',
    'delete': 'perform_destroy'
})
