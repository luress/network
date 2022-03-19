from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    pass

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(blank=True)
    number_of_likes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    create_by_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")

    def serialize(self):
        return {
            "id": self.id,
            "text": self.text,
            "number_of_likes": self.number_of_likes,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "create_by_user": self.create_by_user.username,
        }

class UserFollowing(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User", related_name="following", on_delete=models.CASCADE,default=0)

    following_user_id = models.ForeignKey("User", related_name="followers", on_delete=models.CASCADE, default=0)

    follow_time = models.DateTimeField(auto_now_add=True)

class UserLikes(models.Model):
    id = models.AutoField(primary_key=True)

    user_who_liked = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_who_follow")

    liked_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="liked_post")