from django.http import JsonResponse, HttpResponse
# Create your views here.
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ViewSet, GenericViewSet

from ProductApp.models import Product, ProductPrice
from ProductApp.serializer import ProductSerializer, PriceSerializer


class ProductView(GenericViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer

    def getAllProducts(self, request, *args, **kwargs):
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)

    def addProduct(self, request, *args, **kwargs):
        product_data = JSONParser().parse(request)
        product_data_serializer = ProductSerializer(data=product_data)
        if product_data_serializer.is_valid():
            product_data_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False, status=500)

    def deleteProduct(self, request, *args, **kwargs):
        product_data = JSONParser().parse(request)
        product = Product.objects.get(name=product_data['name'])
        product.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

    def updateProduct(self, request, *args, **kwargs):
        product_data = JSONParser().parse(request)
        product = Product.objects.get(name=product_data['name'])
        product_data_serializer = ProductSerializer(product, data=product_data)
        if product_data_serializer.is_valid():
            product_data_serializer.save()
            return JsonResponse("Edited Successfully!!", safe=False)
        return JsonResponse("Failed to Edit.", safe=False, status=500)


class PriceView(GenericViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = PriceSerializer

    def addPrice(self, request, *args, **kwargs):
        price_data = JSONParser().parse(request)
        price_data_serializer = PriceSerializer(data=price_data)
        try:
            if price_data_serializer.is_valid(raise_exception=True):
                price_data_serializer.save()
                return JsonResponse('Set price Successfully!!', safe=False)
        except Exception as e:
            print(e)
            return JsonResponse(e, safe=False, status=500)

    def calculatePrice(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        product_price_list = ProductPrice.objects.filter(productName=data['productName'])
        product_price_list = product_price_list.filter(startDate__gte=data['startDate'], endDate__lte=data['endDate'])
        sumPrice = 0
        for p in product_price_list:
            print(p.id, p.price)
            sumPrice += p.price
        avgPrice = sumPrice / len(product_price_list)
        return JsonResponse({'price': avgPrice}, safe=False)
