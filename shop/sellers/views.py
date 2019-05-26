from django.shortcuts import HttpResponse
from sellers.models import Seller
from django.template.loader import render_to_string


def show_seller_detail(request, seller_id):
    seller = Seller.objects.get(id=seller_id)

    result = render_to_string('seller.html',{
        'seller': seller,
        'comments': seller.comments.all(),
        'merchandises': seller.merchandises.all(),
    })

    return HttpResponse(result)

