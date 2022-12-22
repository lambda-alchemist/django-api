from django.urls import path, re_path, include
from django.contrib import admin
from rest_framework import routers, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from authentication.views import UserViewSet
from product.views import ProductViewSet, CategoryViewSet
from address.views import AddressViewSet
from cart.views import CartItemViewSet, CartViewSet, PurchaseViewSet

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
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'addr', AddressViewSet)
router.register(r'receit', PurchaseViewSet)
router.register(r'item', CartItemViewSet)
router.register(r'cart', CartViewSet)


urlpatterns = [
	path('', include(router.urls)),
	path('admin/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
	re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
