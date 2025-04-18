from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import post

# Create your tests here.
class test_post(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username = "test", password = "123")
        self.post = post.objects.create(title="test1", description="test2", price=123, seller = self.user)
    def test_string(self):
        p = post(title="ttt")
        self.assertEqual(str(p), p.title)
    def test_model(self):
        self.assertEqual(self.post.title, "test1")
        self.assertEqual(self.post.description, "test2")
        self.assertEqual(self.post.price, 123)
    def test_listview(self):
        res = self.client.get(reverse("post_listview"))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed('post_listview.html')
    def test_detailview(self):
        res = self.client.get("/post/1")
        res2 = self.client.get("/post2/100")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res2.status_code, 404)
        self.assertTemplateUsed(res, "post/post_detailview.html")
    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1')
    def test_createview(self):
        res = self.client.post(reverse('post_createview'),{"title":"test1", "description":"test2", "price":123, "seller": self.user.id})
        self.assertEqual(res.status_code, 302)
        self.assertEqual(post.objects.last().title, "test1")
        self.assertEqual(post.objects.last().description, "test2")
        self.assertEqual(post.objects.last().price, 123)
    def test_updateview(self):
        res = self.client.post(reverse('post_updateview', args="1"), {"title":"test1111", "description":"test2222", "price":123456, "seller": self.user.id})
        self.assertEqual(res.status_code, 302)
    def test_deleteview(self):
        res = self.client.post(reverse('post_deleteview', args="1"))
        self.assertEqual(res.status_code, 302)


