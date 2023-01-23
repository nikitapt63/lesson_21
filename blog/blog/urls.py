from django.contrib import admin
from django.urls import path
from news_feed.views import \
    say_hello, get_pages_list, \
    PostListView, PostCreateView, \
    PostDetailView, PostUpdateView, PostDeleteView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", say_hello),
    path("pages/", get_pages_list),
    path("posts/", PostListView.as_view()),
    path("post_create/", PostCreateView.as_view()),
    path("post/<int:pk>", PostDetailView.as_view()),
    path("post_update/<int:pk>", PostUpdateView.as_view()),
    path("post_delete/<int:pk>", PostDeleteView.as_view()),
]
