from django.urls import path
from .views import cache_example, redis_course

urlpatterns = [
    path('cache/', cache_example),
    path('course/', redis_course),
]
