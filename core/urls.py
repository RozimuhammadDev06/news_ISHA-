from django.urls import path
from .views import index,contact,ctg,src,view,login,register,logout

urlpatterns = [
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
    path("",index, name="home"),
    path("ctg/",ctg, name="ctg"),
    path("ctg/<slug:slug>/",ctg, name="ctg"),
    path("contact/",contact, name="contact"),
    path("src/",src, name="src"),
    path("view/",view, name="view")
]
