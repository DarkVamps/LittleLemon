from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets
from . import models, serielizers


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serielizers.MenuSerializer
    search_fields = ["title"]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serielizers.MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serielizers.BookingSerializer
    search_fields = ["name"]
