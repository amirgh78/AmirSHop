from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def mainpage(request):
    return render(request, 'shop/mainpage.html', {})


def product_list(request):
    products = Product.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'shop/mainpage.html', {'products': products})


def index(request):
    data = Image.objects.all()
    context = {
        'data': data
    }
    return render(request, "mainpage.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/productpage.html', {'product': product})


def userpage(request):
    return render(request, "shop/userpage.html")


def aboutpage(request):
    return render(request, "shop/aboutpage.html")


def contactpage(request):
    return render(request, "shop/contactpage.html")


def cartpage(request):
    return render(request, "shop/cartpage.html")


class HomePageView(TemplateView):
    template_name = 'shop/mainpage.html'


class SearchResultsView(ListView):
    model = Product
    template_name = 'shop/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(
            Q(p_name__icontains=query) | Q(explanation__icontains=query)
        )
        return object_list


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return render(request, "shop/userpage.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="shop/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return render(request, "shop/userpage.html")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="shop/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("shop/mainpage.html")
