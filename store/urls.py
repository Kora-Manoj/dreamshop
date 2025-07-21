from django.urls import path
from .views import HomeView, ProductDetailView ,CartView,AddToCartView,CheckoutView,OrderListView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('orders/', OrderListView.as_view(), name='orders'),
    
]
