from django.test import TestCase

from sodaseo.utils import convert_url


class TestConvertUrl(TestCase):

    def test_function(self):
        url = '/blog/'
        self.assertEqual(convert_url(url), url)

        url = '/blog/?page=1'
        self.assertEqual(convert_url(url), '/blog/?page={{ page }}')

        url = '/blog/?q=super+busca&page=1'
        self.assertEqual(convert_url(url), '/blog/?q={{ q }}&page={{ page }}')

        url = '/blog/?page=1&q=super+busca'
        self.assertEqual(convert_url(url), '/blog/?page={{ page }}&q={{ q }}')

        url = '/blog/?page=1&q=super+busca&limit=10'
        self.assertEqual(
            convert_url(url),
            '/blog/?page={{ page }}&q={{ q }}&limit={{ limit }}'
        )

        url = '/blog/?q=super+busca&page=1&limit=10'
        self.assertEqual(
            convert_url(url),
            '/blog/?q={{ q }}&page={{ page }}&limit={{ limit }}'
        )

        url = '/blog/?a=a&b=b&c=c&d=d&e=e'
        self.assertEqual(
            convert_url(url),
            '/blog/?a={{ a }}&b={{ b }}&c={{ c }}&d={{ d }}&e={{ e }}'
        )

        url = '/blog/?e=e&b=b&c=c&d=d&a=a'
        self.assertEqual(
            convert_url(url),
            '/blog/?e={{ e }}&b={{ b }}&c={{ c }}&d={{ d }}&a={{ a }}'
        )
