from .models import Userr
from rest_framework import viewsets,permissions
from .serializers import UserrSerializers


class UserrViewset(viewsets.ModelViewSet):
    queryset= Userr.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class =UserrSerializers