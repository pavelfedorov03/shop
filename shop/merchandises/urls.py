from django.urls import path

from . import views

urlpatterns = [
    path('merchandises/<int:merchandise_id>/', views.show_merchandise_detail),
]
