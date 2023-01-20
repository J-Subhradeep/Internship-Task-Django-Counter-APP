from rest_framework.serializers import ModelSerializer
from .models import CountDB


class CountDBSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
