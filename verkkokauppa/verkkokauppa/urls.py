"""verkkokauppa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from cart import views as cart_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register-page'),
    path('profile/', user_views.profile, name='profile-page'),    
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), 
         name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), 
         name='logout-page'),
    path('profile/update/', user_views.update, name='update-page'),
    path('contact_us/', user_views.contact, name='contact-page'),
    path('shopping-cart/', cart_views.order_details, name='shopping-cart-page'),
    path('add-to-cart/<int:id>', cart_views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:id>', cart_views.remove_from_cart, 
         name='remove_from_cart'),
    path('shopping-cart/payment/', cart_views.payment_view, name='payment-page'),
    path('shopping-cart/checkout/', cart_views.checkout, name='checkout-page'),
    path('shoppingcart/update-transaction/<int:order_id>', 
         cart_views.update_transaction_records, 
         name='update_transaction_records'),
    path('', include('base.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)