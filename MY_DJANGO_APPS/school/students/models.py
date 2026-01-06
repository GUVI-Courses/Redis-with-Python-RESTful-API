from django.db import models
from django.urls import reverse

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    # Used by Create/Update views to know where to redirect after success
    def get_absolute_url(self):
        return reverse('student_list')