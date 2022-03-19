from django.test import Client, TestCase
from .models import User,UserFollowing, UserLikes, Post
from django.urls import reverse
# Create your tests here.
class PostTestCase(TestCase):

    def setUp(self):
        u1 = User.objects.create(username="example", password="example", email="example@example.com")
        number_of_posts = 30
        for post_id in range(number_of_posts):

            Post.objects.create(text="hello{post_id}", create_by_user=u1)

    
    def text_number_of_likes(self):
        p = Post.objects.get(text="123")
        self.assertEqual(p.number_of_likes, 0)  

    def test_user_create(self):
        u = User.objects.get(username="example")
        self.assertEqual(u.password, "example")

    def test_allposts(self):

        c = Client()

        response = c.get("/posts")

        self.assertEqual(response.status_code, 200)

    def test_allposts_accessible_by_name(self):
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)


    def test_pagination_is_correct(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), 30)