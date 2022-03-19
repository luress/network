import json
import re
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Post, UserFollowing, UserLikes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "network/index.html")

def posts(request):
    #get all posts with ordering by time
    posts = Post.objects.all()
    posts = posts.order_by("-timestamp").all()
    # add pagination fo everi 10 posts
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/allposts.html",{
        "posts": posts,
        "page_obj":page_obj,
        "current_user": request.user,
    })

@login_required
def following_posts(request):
    user = request.user
    #get all following models
    follows = user.following.all()
    #get users which curren user is follow
    ids = [follow_user.following_user_id for follow_user in follows]
    # get sorted posts by following users
    posts = Post.objects.filter(create_by_user__in=ids)
    posts = posts.order_by("-timestamp").all()
    return render(request, "network/following_posts.html",{
        "posts": posts,
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@csrf_exempt
@login_required
def create_post(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    data = json.loads(request.body)
    user = request.user
    text = data.get("text", "")
    post = Post(create_by_user=user, text=text)
    post.save()
    return JsonResponse({"message": "Post created succesfully."}, status=201)


def user_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    current_user = request.user
    is_follow = False
    # check if follow model is created
    if UserFollowing.objects.filter(user_id=current_user, following_user_id=user).exists():
        is_follow = True
    posts = Post.objects.filter(create_by_user=user)
    posts = posts.order_by("-timestamp").all()
    return render(request, "network/profile.html", {
        "user": user,
        "posts": posts,
        "followers": user.followers.all(),
        "following": user.following.all(),
        "current_user": current_user,
        "is_follow": is_follow,
    })


@login_required
def follow(request, user_id):

    following_user = User.objects.get(pk=user_id)
    follower_user = request.user
    #Create new follow model if does not exist
    foll, created = UserFollowing.objects.get_or_create(user_id=follower_user, following_user_id=following_user)    
    return HttpResponseRedirect(reverse("user_profile", args=[user_id]))


@login_required
def unfollow(request, user_id):
    following_user = User.objects.get(pk=user_id)
    follower_user = request.user
    follow_to_delete = UserFollowing.objects.get(user_id=follower_user, following_user_id=following_user)
    follow_to_delete.delete()
    return HttpResponseRedirect(reverse("user_profile", args=[user_id]))


@login_required
@csrf_exempt
def post_edit(request, post_id):

    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found"})

    if request.method == "GET":
        return JsonResponse(post.serialize())

    
    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get("text") is not None:
            post.text = data["text"]
            

        if data.get("number_of_likes") is not None:
            liked_post, created = UserLikes.objects.get_or_create(user_who_liked=request.user, liked_post=post)
            if created == True:
                post.number_of_likes = data["number_of_likes"]
            liked_post.save()
        
        post.save()
        return HttpResponse(status=204)





