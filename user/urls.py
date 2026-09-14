from django.urls import path
from user.views import SellerView, Close

urlpatterns = [
    path('open/', SellerView.as_view()),
    path('close/', Close.as_view()),
]