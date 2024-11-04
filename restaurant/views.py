from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from . import models, serielizers


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class MenuItemView(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = models.Menu.objects.all()
    serializer_class = serielizers.MenuSerializer
    search_fields = ["title"]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = models.Menu.objects.all()
    serializer_class = serielizers.MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = models.Booking.objects.all()
    serializer_class = serielizers.BookingSerializer
    permission_classes = [IsAuthenticated]
