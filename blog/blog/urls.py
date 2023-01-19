from django.contrib import admin
from django.urls import path
from news_feed.views import \
    say_hello, get_pages_list, \
    PostListView, PostCreateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", say_hello),
    path("pages/", get_pages_list),
    path("posts/", PostListView.as_view()),
    path("post_create/", PostCreateView.as_view()),
]
