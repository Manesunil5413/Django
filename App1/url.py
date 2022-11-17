from django.urls import path

from App1 import views

urlpatterns =[
    path('2/',views.function),
    path('read/',views.func)
]