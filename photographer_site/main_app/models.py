from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    class Category(models.TextChoices):
        NONE_CATEGORY = "NoneCategory"
        LANDSCAPE = "Landscape"
        URBAN = "Urban"
        MACRO = "Macro"
        ARISTIC = "Artisctic"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish", default="")
    body = models.TextField()
    image = models.ImageField(upload_to="photo_images", default="")
    featured = models.BooleanField(default=False)
    category = models.CharField(
        max_length=12, choices=Category.choices, default=Category.NONE_CATEGORY
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    liked_by = models.ManyToManyField(User, related_name="post_likes")
    created = models.DateTimeField(default=timezone.now)
    publish = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-publish"]
        indexes = [models.Index(fields=["-publish"])]

    def __str__(self):
        return f"Title: {self.title}"
