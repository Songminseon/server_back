from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListPhone.as_view()),
    path('<int:pk>/', views.DetailPhone.as_view()),
]