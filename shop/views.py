from django.shortcuts import render, get_object_or_404 , redirect, reverse
from .models import Category, Product, ReviewModel
from cart.forms import CartAddProductForm
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import  FormMixin
from django.contrib.auth import  get_user_model

from .forms import  ReviewForm


class HomeView(TemplateView):
    template_name = 'shop/home.html'

class product_list(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/product/list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context

  
    def get(self, request, slug=None):
        products = Product.objects.all()
        if slug:
            cat = Category.objects.get(slug=slug)
            products = Product.objects.filter(category=cat)
            return render(request, 'shop/product/list.html', context={'products':products, 'categories':Category.objects.all()})
        categories = Category.objects.all()
        context = {'products':products, 'categories':categories}
        return render(request, 'shop/product/list.html', context)

    


class product_detail(FormMixin, DetailView):

    model = Product
    context_object_name = 'product'
    template_name = 'shop/product/detail.html'
    form_class = ReviewForm
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('shop:product_detail', kwargs={'id':self.object.id, 'slug':self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        product = self.get_object()
        product_review = ReviewModel.objects.filter(product=product)
        context['product_review'] = product_review
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            product = self.get_object()
            new_review = form.save(commit=False)
            new_review.product = product
            new_review.user = self.request.user
            new_review.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


