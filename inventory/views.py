from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .forms import PasswordResetMockForm, ProductForm
from .models import Product


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True


@login_required

def dashboard(request):
    products = Product.objects.all()
    total_products = products.count()
    total_units = products.aggregate(total=Sum("quantity"))["total"] or 0
    low_stock = products.filter(quantity__gt=0, quantity__lte=10).count()
    out_of_stock = products.filter(quantity=0).count()
    recent_products = products.order_by("-updated_at")[:5]

    categories = list(
        products.values("category").annotate(total=Count("id")).order_by("-total", "category")[:6]
    )

    context = {
        "total_products": total_products,
        "total_units": total_units,
        "low_stock": low_stock,
        "out_of_stock": out_of_stock,
        "recent_products": recent_products,
        "categories": categories,
    }
    return render(request, "inventory/dashboard.html", context)


@login_required

def product_list(request):
    query = request.GET.get("q", "").strip()
    products = Product.objects.all()
    if query:
        products = products.filter(name__icontains=query) | products.filter(sku__icontains=query) | products.filter(category__icontains=query)
    return render(request, "inventory/product_list.html", {"products": products, "query": query})


@login_required

def product_create(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Producto agregado correctamente.")
        return redirect("product_list")
    return render(request, "inventory/product_form.html", {"form": form, "title": "Nuevo producto"})


@login_required

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Producto actualizado correctamente.")
        return redirect("product_list")
    return render(request, "inventory/product_form.html", {"form": form, "title": "Editar producto", "product": product})


@login_required

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Producto eliminado correctamente.")
        return redirect("product_list")
    return render(request, "inventory/product_confirm_delete.html", {"product": product})


def password_reset_mock(request):
    form = PasswordResetMockForm(request.POST or None)
    submitted = False
    if request.method == "POST" and form.is_valid():
        submitted = True
    return render(request, "registration/password_reset_mock.html", {"form": form, "submitted": submitted})
