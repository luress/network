from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["id"]

class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "number_of_likes", "timestamp", "create_by_user"]

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(UserFollowing)
admin.site.register(UserLikes)