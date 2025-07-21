from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, VendorRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('vendor/register/', VendorRegisterView.as_view(), name='vendor_register'),
]
