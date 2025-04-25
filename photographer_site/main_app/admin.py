from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Custom admin panel for the Post model.
    Provides custom layout, display, filters, actions, and preview functionality.
    """

    list_display = (
        "title",
        "author",
        "publish",
        "status_colored",
        "featured",
        "category",
        "image_clickable_preview",
        "view_post_link",
    )
    list_filter = ("status", "created", "publish", "author", "featured", "category")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ("status", "publish")
    actions = ["make_published"]
    readonly_fields = ("created", "publish", "updated", "image_preview_admin")

    fieldsets = (
        (
            "General Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "author",
                    "category",
                    "featured",
                    "status",
                    "liked_by",
                )
            },
        ),
        (
            "Content and Media",
            {
                "fields": (
                    "body",
                    "image",
                    "image_preview_admin",
                )
            },
        ),
        (
            "Dates",
            {
                "fields": (
                    "created",
                    "updated",
                    "publish",
                )
            },
        ),
    )

    @admin.display(description="Image")
    def image_clickable_preview(self, obj):
        """
        Returns an HTML clickable thumbnail preview of the post's image
        for the list display view in the admin panel.

        :param obj: The Post instance.
        :return: Safe HTML with image preview or a "No image" message.
        """
        if obj.image:
            return format_html(
                '<a href="{}" target="_blank">'
                '<img src="{}" width="100" height="60" style="object-fit:cover;" />'
                "</a>",
                obj.image.url,
                obj.image.url,
            )
        return "No image"

    @admin.display(description="Status")
    def status_colored(self, obj):
        """
        Returns the post's status with color formatting.
        Green for Published, gray for Draft.

        :param obj: The Post instance.
        :return: Safe HTML with colored status.
        """
        color = "green" if obj.status == Post.Status.PUBLISHED else "gray"
        return format_html(
            '<span style="color:{}; font-weight:bold;">{}</span>',
            color,
            obj.get_status_display(),
        )

    @admin.display(description="View")
    def view_post_link(self, obj):
        """
        Generates a "Preview" link to view the post on the frontend site
        if the post is published.

        :param obj: The Post instance.
        :return: Safe HTML with preview link or a message if not published.
        """
        if obj.status == Post.Status.PUBLISHED:
            try:
                url = reverse("photo_detail", args=[obj.id])
                return format_html('<a href="{}" target="_blank">Preview</a>', url)
            except:
                return "Missing URL"
        return "Not published"

    @admin.action(description="Publish selected posts")
    def make_published(self, request, queryset):
        """
        Admin action to mark selected posts as Published.

        :param request: The admin request object.
        :param queryset: Queryset of selected posts.
        """
        updated = queryset.update(status=Post.Status.PUBLISHED)
        self.message_user(request, f"{updated} post(s) marked as Published.")

    @admin.display(description="Current Image")
    def image_preview_admin(self, obj):
        """
        Shows a larger preview of the image in the post edit form.

        :param obj: The Post instance.
        :return: Safe HTML with full image preview or message if missing.
        """
        if obj.image:
            return format_html(
                '<img src="{}" width="200" style="object-fit:cover;" />', obj.image.url
            )
        return "No image"
