from django.shortcuts import render

from rest_framework import viewsets

from .models import Flight, Passenger, Reservation

from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer


from rest_framework.permissions import IsAuthenticated
# Create your views here.


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]  

    def perform_create(self, serializer):
        if self.request.user.is_anonymous:
            raise serializers.ValidationError("User must be logged in to create a reservation.")
        serializer.save(user=self.request.user)

    