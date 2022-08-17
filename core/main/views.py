from django.shortcuts import render
from django.views.generic import ListView
from .models import Category
# Create your views here.

class CategoryListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        categories = Category.objects.all()
        return render(request, self.template_name, {'categories':categories})

class BrandListView(ListView):
    template_name = 'brand.html'

    def get(self, request, id):
        brands = Category.objects.filter(pk=id)
        return render(request, self.template_name, {'brands':brands})