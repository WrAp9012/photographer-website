from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("photo_list",views.photo_list, name="post_list"),
    path("<int:id>/", views.photo_detail, name="photo_detail"),
]
