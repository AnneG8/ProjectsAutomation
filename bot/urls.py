from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('choose-students/', views.choose_students, name='choose_students'),
    path('send-message/', views.send_message, name='send_message'),
]