from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm

# READ: Lists all students (student_list.html)
class StudentListView(ListView):
    model = Student
    # The default template name is 'students/student_list.html', which matches the file structure
    
# CREATE: Adds a new student (student_form.html)
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    # We specify the template name here to match 'student_form.html'
    template_name = 'students/student_form.html'
    
# UPDATE: Edits an existing student (student_form.html)
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'

# DELETE: Deletes a student
class StudentDeleteView(DeleteView):
    model = Student
    # Success URL to redirect to after deletion
    success_url = reverse_lazy('student_list')
    # Use a default confirmation template or create a custom one if needed