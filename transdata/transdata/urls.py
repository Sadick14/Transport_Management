from django.contrib import admin
from django.urls import path, include  # Import the include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stc.urls')),  # Include the URLs from your 'stc' app
]
