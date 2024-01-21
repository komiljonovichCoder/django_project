from django.urls import path
from .views import index, main, about, contact

urlpatterns = [
    path('index/', index, name='index'),
    path('main/', main, name='main'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact')
]
