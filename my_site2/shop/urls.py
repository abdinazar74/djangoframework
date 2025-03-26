from django.urls import path
from .views import CategoryViewSets, ProductViewSets


urlpatterns = [
    path('', ProductViewSets.as_view({'get': 'list'}))
]