from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Brand, Watch, Profile,Cart
from django.core.validators import MaxValueValidator, MinValueValidator


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Watch
        fields= ['brand','model_name', 'water_resistance', 'manufacture_year', 'price', 'availability','image']

class WatchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Watch
        exclude= ['user']


#comments & ratings and profile
class CommentSerializer(serializers.Serializer):
    class Meta:
        email = serializers.EmailField()
        content = serializers.CharField(max_length=200, required=True)
        created = serializers.DateTimeField()

class RatingSerializer(serializers.Serializer):
    class Meta:
        Rating = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

class ProfileSerializer(serializers.ModelSerializer):
    comment= CommentSerializer()
    rating= RatingSerializer()
    class Meta:
        model= Profile
        fields=['user','comment','rating']

   # def get_rating(self,obj):
   #  rating= (obj*5)/100
   #  ##
   #  return rating
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['watch']
        
