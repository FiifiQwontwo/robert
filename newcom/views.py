from django.shortcuts import render
from .models import *
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from django.views.generic import View
from .serializer import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def id_list(request):
    if request.method == 'GET':
        art = Ids.objects.all()
        serializer = IdsSerializer(art, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IdsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def id_detail(request, pk):
    try:
        artis = Ids.objects.get(pk=pk)
    except Ids.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IdsSerializer(artis)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = IdsSerializer(artis, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artis.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        procat = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(procat, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductCategory(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def productdetails(request, pk):
    try:
        prod = ProductCategory.objects.get(pk=pk)
    except ProductCategory.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductCategorySerializer(prod)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductCategorySerializer(prod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        prod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
