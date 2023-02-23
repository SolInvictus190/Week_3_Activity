import json
from django.http import JsonResponse, HttpResponse
from product.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def api_home(request, *args, **kwargs):


    if model_data:
       data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return Response(data)