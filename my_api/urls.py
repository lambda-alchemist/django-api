from django.urls import path, include
from rest_framework import routers
from authentication.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'api/v1/users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
