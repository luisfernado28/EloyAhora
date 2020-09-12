from django.urls import path
from .views import *


urlpatterns = [
    path('users/', user_list),
    path('product/', ProductAPIView.as_view()),
    path('usersdetail/<int:pk>/', user_detail),
]
