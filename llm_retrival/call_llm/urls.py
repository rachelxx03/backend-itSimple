from django.urls import path
from . import views
from .views import CustomObjectAPIView

urlpatterns = [
    path("", views.home, name="home"),
    path('your-endpoint/', CustomObjectAPIView.as_view(), name='custom-object'),

]
