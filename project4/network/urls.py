
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("posts", views.posts, name="posts"),
    path("posts/<int:post_id>", views.post_edit, name="edit"),
    path("posts/create_post", views.create_post, name = "create_post"),
    path("posts/following_posts", views.following_posts, name="following_posts"),
    path("profile/<int:user_id>", views.user_profile, name="user_profile"),
    path("profile/<int:user_id>/follow", views.follow, name="follow"),
    path("profile/<int:user_id>/unfollow", views.unfollow, name="unfollow"),
]
