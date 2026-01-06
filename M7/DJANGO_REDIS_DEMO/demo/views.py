from django.http import HttpResponse
from django.core.cache import cache

def cache_demo(request):
    cache.set('greeting', 'Hello Redis Cache!', timeout=30)
    value = cache.get('greeting')
    return HttpResponse(f"Cached Value: {value}")

def course_demo(request):
    cache.set('course', 'Django with Redis', timeout=60)
    course_name = cache.get('course')
    return HttpResponse(f"Course: {course_name}")
