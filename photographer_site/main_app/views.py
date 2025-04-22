from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from main_app.models import Post

# Create your views here.


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page", 1)

    try:
        post = paginator.page(page_number)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    return render(request, "main_app/post/list.html", {"post": post})
