from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = "main_app"

urlpatterns: list[URLPattern] = [
    path("", views.main_page, name="home"),
    path("photo_list", views.photo_list, name="post_list"),
    path("<int:id>/", views.photo_detail, name="photo_detail"),
    path("galery/", views.photo_list, name="galery"),
    path("contact/", views.contact, name="contact"),
    path("about_me/", views.about_me, name="about_me"),
]
