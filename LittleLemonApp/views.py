from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from LittleLemonApp.forms import CommentForm
from .models import UserComments
from django.http import JsonResponse

# Create your views here.


def form_view(request):
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            uc = UserComments(
                first_name=cd["first_name"],
                last_name=cd["last_name"],
                comment=cd["comment"],
            )
            uc.save()
            return JsonResponse({"message": "success"})

    return render(request, "blog.html", {"form": form})
