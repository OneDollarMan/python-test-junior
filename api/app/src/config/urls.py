from django.urls import path, include
from src.app.controller import EventController

urlpatterns = [
    path('event/', EventController.as_view({'get': 'get_result', 'post': 'create'})),
]