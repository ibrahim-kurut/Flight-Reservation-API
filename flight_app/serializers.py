from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Flight, Passenger, Reservation



class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'
        read_only_fields = ("create_date",)


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    passenger = PassengerSerializer()
    flight_number = serializers.CharField(write_only=True)
    flight_number_display = serializers.CharField(source='flight.flight_number', read_only=True)

    class Meta:
        model = Reservation
        fields = ['flight_number', 'flight_number_display', 'passenger', 'user']


    def create(self, validated_data):
        flight_number = validated_data.pop('flight_number')
        try:
            flight = Flight.objects.get(flight_number=flight_number)
        except Flight.DoesNotExist:
            raise serializers.ValidationError("Flight with this flight number does not exist.")
        
        passenger_data = validated_data.pop('passenger')
        passenger = Passenger.objects.create(**passenger_data)
        
        reservation = Reservation.objects.create(flight=flight, passenger=passenger, **validated_data)
        return reservation
