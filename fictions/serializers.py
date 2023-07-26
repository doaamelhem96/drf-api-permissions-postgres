from rest_framework import serializers
from .models import Fiction

class FictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fiction
        fields =['id','owner', 'name', 'gener']
       


 