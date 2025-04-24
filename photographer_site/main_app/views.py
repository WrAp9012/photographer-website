from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from main_app.models import Post

# Create your views here.


def main_page(request):
    photo_list = Post.published.all().filter(featured=True)

    return render(
        request, "main_app/photo_gallery/photo_main_site.html", {"photos": photo_list}
    )


def photo_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page", 1)

    try:
        photos = paginator.page(page_number)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    return render(request, "main_app/photo_gallery/photo_list.html", {"photos": photos})


def photo_filter(request, photo_category):
    photo_category_list = Post.published.all().filter(category=photo_category)
    return render(
        request,
        "main_app/photo_gallery/photo_category.html",
        {"photos": photo_category_list, "category": photo_category},
    )


def photo_detail(request, id):
    photo = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)

    return render(request, "main_app/photo_gallery/photo_detail.html", {"photo": photo})


def contact(request):
    return render(request, "main_app/photo_gallery/contact.html")


def about_me(request):
    return render(request, "main_app/photo_gallery/aboutme.html")
