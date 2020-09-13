from django.urls import path
from .views import *


urlpatterns = [
    path('product/', ProductAPIView.as_view()),
    path('productdetail/<int:id>/', ProductDetails.as_view()),

    path('users/', user_list),
    path('usersdetail/<int:pk>/', user_detail),
]
