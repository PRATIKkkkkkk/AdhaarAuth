from django.urls import path

from .views import AdhaarAuthView

urlpatterns = [
    path('', AdhaarAuthView.as_view())  
]