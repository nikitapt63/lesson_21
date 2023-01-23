from django.db import models
from django.contrib.auth.models import User


class DateTimeMixin:
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Page(models.Model, DateTimeMixin):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        ordering = ["title"]


class Post(models.Model, DateTimeMixin):
    name = models.CharField(max_length=100)
    content = models.TextField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.name}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["name"]
