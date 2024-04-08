from django.db import models

class DepartureTime(models.Model):
    dept_time = models.CharField(max_length=50)
    time = models.DateTimeField()

    def __str__(self):
        return f'{self.time} {self.dept_time}'

class Vehicle(models.Model):
    drivers_name = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=20, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    dept_time = models.ForeignKey(DepartureTime, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.make} {self.model} ({self.year}) - {self.registration_number}'

class Route(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.email} {self.phone}'

class TicketRecord(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dept_time = models.ForeignKey(DepartureTime, on_delete=models.CASCADE)
    date = models.DateField()
    ticket_number = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.vehicle} - {self.route} {self.customer} {self.dept_time} {self.price} {self.date}'

