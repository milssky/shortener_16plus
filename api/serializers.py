from rest_framework.serializers import ModelSerializer

from shortener.models import Url


class UrlSerilizer(ModelSerializer):
    class Meta:
        model = Url
        fields = "__all__"
