from django.contrib import admin
from django.urls import path, include
from canchas.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('canchas/', include('canchas.urls')),
]