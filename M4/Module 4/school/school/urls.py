from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Map all URLs starting with 'students/' to the students app's urls.py
    path('students/', include('students.urls')),
]