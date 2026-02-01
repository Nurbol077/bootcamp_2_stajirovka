from django.urls import path
from .views import product_list, product_detail, product_delete
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet

# urlpatterns = [
#     # path('products/', product_list),
#     # path('products/<int:pk>/', product_detail),
#     # path('products/<int:pk>/delete/', product_delete),
#     # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
#     # path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
#     path('api/', ProductViewSet.as_view(url_name='products')),
# ]

router = DefaultRouter()
router.register(r'products', ProductViewSet)
urlpatterns = router.urls