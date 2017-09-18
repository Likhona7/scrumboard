from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializer import ListSerialiser, CardSerializer
from .models import List, Card


class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerialiser
    permission_classes = (permissions.IsAuthenticated,)



class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticated,)