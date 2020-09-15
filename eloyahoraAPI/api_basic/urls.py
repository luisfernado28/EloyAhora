from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('product',ProductViewSet, basename='product')

urlpatterns = [

    path('tags/<int:id>/', GenericAPIView.as_view()),

    path('', include(router.urls)),
    path('<int:id>/', include(router.urls)),
    #path('product/<int:id>/', ProductDetails.as_view()),

    path('users/', user_list),
    path('usersdetail/<int:pk>/', user_detail),
]
