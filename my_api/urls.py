import django
from django.urls import path, re_path, include
from django.contrib import admin, admindocs
from rest_framework import routers, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from authentication.views import UserViewSet
from product.views import ProductViewSet, CategoryViewSet, AddressViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
	openapi.Info(
	title="Snippets API",
		default_version='v1',
		description="Test description",
		terms_of_service="https://www.google.com/policies/terms/",
		contact=openapi.Contact(email="contact@snippets.local"),
		license=openapi.License(name="BSD License"),
	),
	public=True,
	permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'api/v1/users', UserViewSet)
router.register(r'api/v1/products', ProductViewSet)
router.register(r'api/v1/category', CategoryViewSet)
router.register(r'api/v1/address', AddressViewSet)


urlpatterns = [
	path('', include(router.urls)),
	path('admin/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
	re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
