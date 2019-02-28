from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from padelAPI.models import Reservation
from . import serializers


class ListReservation(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer


class DetailReservation(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer

