from django.shortcuts import render, redirect
from .forms import VehicleForm, RouteForm, CustomerForm, TicketRecordForm, DepartureTimeForm

def vehicle_form_view(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = VehicleForm()
    return render(request, 'vehicle_form.html', {'form': form})

def route_form_view(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = RouteForm()
    return render(request, 'route_form.html', {'form': form})

def customer_form_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

def ticket_record_form_view(request):
    if request.method == 'POST':
        form = TicketRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TicketRecordForm()
    return render(request, 'ticket_record_form.html', {'form': form})

def departure_time_form_view(request):
    if request.method == 'POST':
        form = DepartureTimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DepartureTimeForm()
    return render(request, 'departure_time_form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def home(request):
    return render(request, 'home.html')


