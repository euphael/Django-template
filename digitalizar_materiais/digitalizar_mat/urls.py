from django.urls import path
from .views import soma, index

urlpatterns = [
    path('', index, name='index'),
    path('soma/', soma, name='soma'),
]