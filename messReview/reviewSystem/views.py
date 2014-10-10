from reviewSystem.models import Item,Category,User,Rating
from reviewSystem.serializers import ItemSerializer,CategorySerializer,UserSerializer,RatingSerializer
#from django.shortcuts import render
#from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Create your views here.
class ItemA(APIView):
	# authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request, format=None):
		item = Item.objects.all()
		serializer = ItemSerializer(item, many=True)
		return Response(serializer.data)
