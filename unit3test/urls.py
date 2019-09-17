from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('main_app.urls')),
    path('admin/', admin.site.urls),
]