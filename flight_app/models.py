from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Flight(models.Model):


    # Operation airlines choices
    operation_airlines = (
        ('Air France', 'Air France'),
        ('KLM', 'KLM'),
        ('Lufthansa', 'Lufthansa'),
        ('British Airways', 'British Airways'),
        ('Emirates', 'Emirates'),
    )



    flight_number = models.CharField(max_length=100)
    operation_airlines = models.CharField(max_length=100, choices=operation_airlines)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    date_of_departure = models.DateField()
    estimated_time_of_departure = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return f"flight_number {self.flight_number} from {self.departure_city} to {self.arrival_city}"



class Passenger(models.Model):

    # Added passenger type
    TYPE_CHOICES = (
        ('Adult', 'Adult'),
        ('Child', 'Child'),
        ('Infant', 'Infant'),
        )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    create_date = models.DateTimeField(auto_now_add=True)
    passenger_type = models.CharField(max_length=10, choices=TYPE_CHOICES)  
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.passenger_type})"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation by {self.user} for {self.passenger} on flight {self.flight}"



