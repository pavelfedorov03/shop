from django.template.loader import render_to_string
from django.shortcuts import HttpResponse

from merchandises.models import Merchandise


def show_main_page(request):
    merchandises = Merchandise.objects.all()

    result = render_to_string('index.html', {
        'merchandises': merchandises,
    })

    return HttpResponse(result)

