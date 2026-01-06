from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # Fields to include in the form
        fields = ['name', 'student_id', 'email', 'date_of_birth']
        
        # Optional: Add custom labels and widgets
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }