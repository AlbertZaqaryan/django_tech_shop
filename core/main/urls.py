from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='home'),
    path('<int:id>', views.BrandListView.as_view(), name='brand'),
]