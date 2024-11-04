from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import bleach
from . import models


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = "__all__"
