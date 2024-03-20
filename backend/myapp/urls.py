from django.urls import path
from . import views

urlpatterns = [
    path('uploadCSV/', views.uploadCSV),
    path('hello/', views.sayHello),
    path('upload_file/', views.upload_file)
]