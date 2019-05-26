from django.shortcuts import HttpResponse
from merchandises.models import Merchandise
from django.template.loader import render_to_string


def show_merchandise_detail(request, merchandise_id):
    merchandise = Merchandise.objects.get(id=merchandise_id)
    result = render_to_string('merchandise.html',{
        'merchandise': merchandise,
    })

    return HttpResponse(result)



