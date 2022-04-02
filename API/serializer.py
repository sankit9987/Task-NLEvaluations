from rest_framework import serializers
from main.models import *

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apps
        fields = ['img','app_name','app_link','category','sub_category','point']