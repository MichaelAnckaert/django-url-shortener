from django.http.response import Http404
from django.test import RequestFactory, TestCase

from shorturl.models import ShortendUrl
from shorturl.views import go_to_url


class RedirectTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_redirect_found(self):
        url = ShortendUrl.objects.create(destination_url="https://sinax.be")

        request = self.factory.get(f"/g/{url.id}")
        response = go_to_url(request, url.id)

        self.assertEquals(response.url, url.destination_url)

    def test_redirect_not_found(self):
        request = self.factory.get("/g/99999")
        self.assertRaises(Http404, go_to_url, request, pk=99999)
