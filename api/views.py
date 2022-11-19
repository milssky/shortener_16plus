from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.serializers import UrlSerilizer
from api.permissions import HaveSecretWordOrReadOnly
from shortener.models import Url


class UrlViewSet(ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerilizer
    permission_classes = (HaveSecretWordOrReadOnly,)




# class CommentViewSet(ModelViewSet):
#     serializer_class = ...
#     permission_classes = ...

#     def get_queryset(self):
#         post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))  # post_id -- параметр ссылки. post/<post_id>/comments
#         return post.comments