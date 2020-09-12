from django.urls import path
from .views import *


urlpatterns = [
    path('users/', user_list),
    path('detail/<int:pk>/', user_detail),
]
