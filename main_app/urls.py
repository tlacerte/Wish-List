from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.CreateWish.as_view(), name='create'),
    path('delete/<int:pk>', views.DeleteWish.as_view(), name='delete'),
]