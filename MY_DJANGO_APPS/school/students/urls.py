from django.urls import path
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    # Read/List URL
    path('', StudentListView.as_view(), name='student_list'),
    
    # Create URL
    path('new/', StudentCreateView.as_view(), name='student_create'),
    
    # Update URL (uses primary key 'pk' to identify the student)
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='student_update'),
    
    # Delete URL
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
]