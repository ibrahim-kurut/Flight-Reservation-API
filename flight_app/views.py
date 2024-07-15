from django.shortcuts import render

from rest_framework import viewsets

from .models import Flight, Passenger, Reservation

from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer

from .permissions import IsAdminOrReadOnly, IsOwnerOrAdmin


from rest_framework.permissions import IsAuthenticated
# Create your views here.


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAdminOrReadOnly]


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated,IsAdminOrReadOnly]


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin] 

    def perform_create(self, serializer):
        if self.request.user.is_anonymous:
            raise serializers.ValidationError("User must be logged in to create a reservation.")
        serializer.save(user=self.request.user)

    