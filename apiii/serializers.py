from rest_framework import serializers
from .models import Userr

class UserrSerializers(serializers.ModelSerializer):
    class Meta:
        model= Userr
        fields=("user","permiso")
        read_only_fields=("create", )