from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy

# Create your views here.


class TopView(TemplateView):
    template_name = "crud/top.html"


class ProductListView(ListView):
    template_name = "crud/product_list.html"
    model = Product
    paginate_by = 3


class ProductCreateView(CreateView):
    template_name = "crud/product_form.html"
    model = Product
    fields = "__all__"


class ProductUpdateView(UpdateView):
    template_name = "crud/product_update_form.html"
    model = Product
    fields = "__all__"


class ProductDeleteView(DeleteView):
    template_name = "crud/confirm_delete.html"
    model = Product
    success_url = reverse_lazy("list")


class ProductDitailView(DetailView):
    template_name = "crud/product_detail.html"
    model = Product
