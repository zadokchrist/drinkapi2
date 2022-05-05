import re
from rest_framework.views import View
from . serializers import DrinkSerializer
from . models import Drink
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#receive get request
#serialize the request
#return json response
@api_view(['GET','POST'])
def detail_view(request):
    if request.method == 'GET':
        drink = Drink.objects.all()
        seriliser = DrinkSerializer(drink,many=True)
        return Response(seriliser.data,status=status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        seriliser = DrinkSerializer(data=request.data)
        if seriliser.is_valid():
            seriliser.save()
            return Response(seriliser.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#delete specific item in the db
#return response
@api_view(['GET','DELETE','PUT'])
def detail_list(request,id):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = DrinkSerializer(drink,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

