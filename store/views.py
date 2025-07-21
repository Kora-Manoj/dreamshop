from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages 

from .models import Product, Order, CartItem  # ✅ Using CartItem

class HomeView(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'


from django.views import View
from django.shortcuts import render
from .models import CartItem

class CartView(View):
    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.total_price for item in cart_items)
        return render(request, 'store/cart.html', {
            'cart_items': cart_items,
            'total_price': total,
        })



class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product
        )
        if not created:
            cart_item.quantity += 1
        cart_item.save()
        return redirect('cart')

    def get(self, request, pk):
        return self.post(request, pk)


class CheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        grand_total = sum(item.total_price for item in cart_items)
        return render(request, 'store/checkout.html', {
            'cart_items': cart_items,
            'grand_total': grand_total
        })

    def post(self, request):
        cart_items = CartItem.objects.filter(user=request.user)

        if not cart_items.exists():
            messages.error(request, "Your cart is empty.")
            return redirect('cart')

        for item in cart_items:
            Order.objects.create(
                user=request.user,
                product=item.product,
                quantity=item.quantity
            )

        cart_items.delete()  # 🔥 Clear the cart

        messages.success(request, "Order placed successfully!")
        return redirect('orders')


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'store/orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-ordered_at')
