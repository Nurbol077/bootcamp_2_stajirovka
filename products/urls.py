from django.urls import path
from .views import product_list, product_detail, product_delete

urlpatterns = [
    path('products/', product_list),
    path('products/<int:pk>/', product_detail),
    path('products/<int:pk>/delete/', product_delete)
]