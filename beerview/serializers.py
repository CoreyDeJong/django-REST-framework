
from rest_framework import serializers
from .models import Beer

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = ('id','title','body','author')