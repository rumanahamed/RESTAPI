from django.shortcuts import render
from rest_framework import response
from rest_framework.views import Response
from rest_framework.views import APIView
from .serializers import Product_Serializers,Serializer_Serializer
from .models import Product
from django.http import Http404

class Product_Detail(APIView):
    def post(self,request):
        product_instance = Product_Serializers(data=request.data)
        if product_instance.is_valid():
            product_instance.save()
            return Response(product_instance.data)
        return Response(product_instance.errors)

class Product_list_view(APIView):
    def get(self, request, format=None):
        snippets = Product.objects.all()  #fetching the data from table(i.e Product)
        serializer = Serializer_Serializer(snippets, many=True)
        return Response(serializer.data)

class Product_detail_view(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Product_Serializers(snippet)
        return Response(serializer.data)
