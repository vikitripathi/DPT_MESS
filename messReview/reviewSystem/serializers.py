from rest_framework import serializers
from reviewSystem.models import Item,Category,User,Rating

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('id', 'item_name', 'item_rating', 'item_id')


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('id', 'item', 'items_type')


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('id', 'user_id','first_name', 'last_name', 'email','tiemstamp')


class RatingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('id', 'item', 'ratings', 'timestamp','user')						