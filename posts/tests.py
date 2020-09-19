from django.test import TestCase

from django.contrib.auth.models import User

from .models import Post

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        ts1 = User.objects.create_user(
            username='ts1', password='abc123'
        )
        ts1.save()

        test_post = Post.objects.create(
            author=ts1, title='Blog Title', body='Body Content'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'ts1')
        self.assertEqual(title, 'Blog Title')
        self.assertEqual(body, 'Body Content')
