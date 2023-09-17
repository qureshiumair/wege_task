from rest_framework import serializers
from .models import UserInfoTable


class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfoTable
        fields = ('username','email','user_category')
