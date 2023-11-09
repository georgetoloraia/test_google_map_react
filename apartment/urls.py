from rest_framework.routers import DefaultRouter
from .views import ApartmentViewSet
from django.urls import path , include



router = DefaultRouter()
router.register(r'apartments' , ApartmentViewSet )

urlpatterns = [
    path('' , include(router.urls))
]