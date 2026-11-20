from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from  .models import New,Category
from django.db.models import Q
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.db import IntegrityError, transaction
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.decorators.cache import never_cache
from .forms import LoginForm, RegisterForm



import secrets
from django.conf import settings
from django.core.mail import send_mail


@never_cache
def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = RegisterForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        try:
            with transaction.atomic():
                user = form.save()
                code = f"{secrets.randbelow(1000000):06d}"

                send_mail(
                    subject="Tasdiqlash kodi",
                    message=f"Szining kodiz {code}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                )
        
        except IntegrityError:
            form.add_error("phone_number", "Bu telefon raqami bilan hisob allaqachon ochilgan.")
        else:
            auth_login(request, user, backend="core.backends.PhoneBackend")
            return redirect("home")
    return render(request, "register.html", {"form": form})


@never_cache
def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = LoginForm(request, data=request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        auth_login(request, form.user)
        return redirect("home")
    return render(request, "login.html", {"form": form})



@require_POST
def logout(request):
    auth_logout(request)
    return redirect("home")

def index(request):
    last_new = New.objects.order_by("-id").first()
    pp_new = New.objects.order_by("-views")[:4]
    ctg = Category.objects.filter(is_menu=True)
    J_new =  New.objects.filter(category__cat_name="Jahon")
    sport_news = New.objects.filter(category__cat_name="Sport")
    Qaynoq_new = list(New.objects.select_related("category").order_by("-id")[:12])
    qaynoq_pages = [Qaynoq_new[i:i + 4] for i in range(0, len(Qaynoq_new), 4)]
    big_news = New.objects.filter(category__cat_name="Iqtisod").first()
    Iqtisod_news = New.objects.filter(category__cat_name="Iqtisod")[1:5]
    uzbekistan_news = list(New.objects.select_related("category").filter(category__slug="ozbekiston")[:12])



    ctx = {
        "last_new":last_new,
        "pp_new":pp_new,
        "ctg":ctg,
        "J_new":J_new,
        "sport": sport_news,
        "Qaynoq_new": Qaynoq_new,
        "qaynoq_pages": qaynoq_pages,
        "Iqtisod_news":Iqtisod_news,
        "big": big_news,
        "uzbekistan_featured": uzbekistan_news[:2],
        "uzbekistan_columns": [uzbekistan_news[2:7], uzbekistan_news[7:12]],
    }
    return render(request,"index.html",ctx)

def ctg(request, slug=None):
    category = get_object_or_404(Category, slug=slug) if slug else None
    news = New.objects.select_related("category").order_by("-created_at", "-id")
    if category:
        news = news.filter(category=category)
    ctx = {
        "ctg": Category.objects.filter(is_menu=True),
        "category": category,
        "page_obj": Paginator(news, 6).get_page(request.GET.get("page")),
        "popular_news": news.order_by("-views", "-id")[:4],
    }
    return render(request,"category.html",ctx)


def contact(request):
    ctx = {}
    return render(request,"contact.html",ctx)

def src(request):

    search =  request.GET.get("search","").strip()
    news = New.objects.none()

    if search:
        news =  New.objects.filter(
            Q(title__icontains=search)
            | Q(short_desc__icontains=search)
            | Q(description__icontains=search)
        ).select_related("category").order_by("-created_at", "-id")




    ctx = {
        "search":search,
        "page_obj": Paginator(news, 6).get_page(request.GET.get("page")),
    }
    return render(request,"search.html",ctx)

def view(request):
    ctx = {}
    return render(request,"view.html",ctx)
























































