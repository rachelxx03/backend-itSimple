from django.urls import path
from . import views
from .views import ReturnTwoAPIView

urlpatterns = [
    path("", views.home, name="home"),
    path('return-two/', ReturnTwoAPIView.as_view(), name='return-two'),
]
