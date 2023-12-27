from django.test import TestCase
from .models import Post , Category
from django.contrib.auth.models import User

# Create your tests here.

class BlogModelTest(TestCase):

    def post_create(self):
        author = User.objects.create(username='test',password='test123')
        category = Category.objects.create(name='test c')

        return Post.objects.create(
            author = author ,
            title = 'test t',
            tags = 'django',
            description = 'python django',
            category = category
        )

    def test_model_str(self):
      post = self.post_create()
      self.assertEqual(post.__str__(),post.title)


class BlogViewTest(TestCase):

    def test_blog_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code)