from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Beer

class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_beer = Beer.objects.create(
            author = test_user,
            title = 'Title of Beer',
            body = 'Words about da beerz'
        )
        test_beer.save()

    def test_beer_content(self):
        post = Beer.objects.get(id=1)
        

        self.assertEqual(str(post.author), 'tester')
        self.assertEqual(post.title, 'Title of Beer')
        self.assertEqual(post.body, 'Words about da beerz')