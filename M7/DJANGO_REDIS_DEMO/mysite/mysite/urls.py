from django.contrib import admin
from django.urls import path
from demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cache/', views.cache_demo, name='cache_demo'),
    path('course/', views.course_demo, name='course_demo'),
]
