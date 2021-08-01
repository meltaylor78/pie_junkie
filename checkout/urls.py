from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_successful/<order_number>', views.checkout_success, name='checkout_successful'),
    path('wh/', webhook, name='webhook')
]