from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Beer

class BeerModelTests(TestCase):

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
        beer = Beer.objects.get(id=1)
        expected_author = f'{beer.author}'
        expected_title = f'{beer.title}'
        expected_body = f'{beer.body}'

        self.assertEqual(str(beer.author), 'tester')
        self.assertEqual(beer.title, 'Title of Beer')
        self.assertEqual(beer.body, 'Words about da beerz')