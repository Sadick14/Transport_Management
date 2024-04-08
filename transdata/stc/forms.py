from django import forms
from .models import Vehicle, Route, Customer, TicketRecord, DepartureTime

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['drivers_name', 'registration_number', 'make', 'model', 'dept_time', 'capacity']

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['name', 'description']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']

class TicketRecordForm(forms.ModelForm):
    class Meta:
        model = TicketRecord
        fields = ['customer', 'vehicle', 'route', 'price', 'dept_time', 'date', 'ticket_number']

class DepartureTimeForm(forms.ModelForm):
    class Meta:
        model = DepartureTime
        fields = ['dept_time', 'time']
