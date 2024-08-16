from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('digitalizar_mat.urls')),  # Certifique-se de que 'digitalizar_mat' é o nome correto do seu aplicativo
]