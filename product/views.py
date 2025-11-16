from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Product, ProductCategory
from .forms import ProductForm, CategoryForm

# ---- PRODUCT LIST ----
@login_required
def product_list(request):
    print(request.user.get_all_permissions())
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})


# ---- PRODUCT DETAILS ----
@login_required
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "products/detail.html", {"product": product})


# ---- CREATE PRODUCT ----
@login_required
@permission_required("product.add_product", raise_exception=True)
def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            p = form.save(commit=False)
            p.created_by = request.user
            p.updated_by = request.user
            p.save()
            return redirect("products:list")
    else:
        form = ProductForm()
    return render(request, "products/add.html", {"form": form})


# ---- EDIT PRODUCT ----
@login_required
@permission_required("product.change_product", raise_exception=True)
def product_edit(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            p = form.save(commit=False)
            p.updated_by = request.user
            p.save()
            return redirect("product:detail", slug=product.slug)
    else:
        form = ProductForm(instance=product)
    return render(request, "products/edit.html", {"form": form, "product": product})


# ---- CATEGORY MANAGEMENT ----
@login_required
@permission_required("product.add_productcategory", raise_exception=True)
def category_add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products:list")
    else:
        form = CategoryForm()
    return render(request, "products/category_add.html", {"form": form})