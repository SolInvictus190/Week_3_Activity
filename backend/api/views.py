
from product.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializers import ProductSerializer
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        # data = serializer.data
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     data = ProductSerializer(instance).data
    #    # data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
        return Response(serializer.data)
    return Response({"Invalid": "not good data"}, status=400)