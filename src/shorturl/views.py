from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from shorturl.models import ShortendUrl


def go_to_url(request, pk: int) -> HttpResponseRedirect:
    url: ShortendUrl = get_object_or_404(ShortendUrl, pk=pk)

    return HttpResponseRedirect(url.destination_url)
