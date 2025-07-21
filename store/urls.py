from django.urls import path
from .views import HomeView, ProductDetailView ,CartView,AddToCartView,CheckoutView,OrderListView,VendorDashboardView,ProductCreateView,ProductUpdateView,ProductDeleteView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('vendor/dashboard/', VendorDashboardView.as_view(), name='vendor_dashboard'),
    path('vendor/product/add/', ProductCreateView.as_view(), name='vendor_product_create'),
    path('vendor/product/<int:pk>/edit/', ProductUpdateView.as_view(), name='vendor_product_update'),
    path('vendor/product/<int:pk>/delete/', ProductDeleteView.as_view(), name='vendor_product_delete'),
    
]
