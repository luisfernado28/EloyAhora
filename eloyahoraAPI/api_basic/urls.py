from django.urls import path
from .views import *


urlpatterns = [

    path('tags/<int:id>/', GenericAPIView.as_view()),

    path('product/', ProductAPIView.as_view()),
    path('productdetail/<int:id>/', ProductDetails.as_view()),

    path('users/', user_list),
    path('usersdetail/<int:pk>/', user_detail),
]
