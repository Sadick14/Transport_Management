from django.urls import path
from stc import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicle/form/', views.vehicle_form_view, name='vehicle_form'),
    path('route/form/', views.route_form_view, name='route_form'),
    path('customer/form/', views.customer_form_view, name='customer_form'),
    path('ticketrecord/form/', views.ticket_record_form_view, name='ticket_record_form'),
    path('departuretime/form/', views.departure_time_form_view, name='departure_time_form'),
    path('success/', views.success_view, name='success'),
    # Add more URL patterns as needed
]
