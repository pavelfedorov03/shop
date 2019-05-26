from django.urls import path

from . import views

urlpatterns = [
    path('sellers/<int:seller_id>/', views.show_seller_detail),
]
