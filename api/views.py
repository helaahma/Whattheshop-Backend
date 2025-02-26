from rest_framework.generics import (RetrieveUpdateAPIView,ListAPIView, RetrieveAPIView,CreateAPIView, DestroyAPIView)
from rest_framework.views import APIView
from .serializers import (WatchUpdateSerializer,CreateSerializer,CheckoutSerializer,CartSerializer, UserCreateSerializer, WatchListSerializer, CartListSerializer, WatchDetailSerializer, ProfileSerializer, ProfileDetailSerializer)
from rest_framework.filters import (SearchFilter, OrderingFilter,)
from .models import ( Watch,Profile, Cart,)
from .permissions import IsWatchOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status




class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ProfileUpdate(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

class ProfileDetail(RetrieveAPIView):
    serializer_class = ProfileDetailSerializer
    permission_classes = [IsAuthenticated]


    def get_object(self):
        return self.request.user.profile


class WatchList(ListAPIView):
    queryset = Watch.objects.all()
    serializer_class = WatchListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['model_name', 'brand', 'price', 'availability']

class WatchDetail(RetrieveAPIView):
    queryset = Watch.objects.all()
    serializer_class = WatchDetailSerializer 
    lookup_field = 'id'
    lookup_url_kwarg = 'watch_id'

# class UpdateWatch(RetrieveUpdateAPIView):
#     queryset = Watch.objects.all()
#     lookup_field = 'id'
#     lookup_url_kwarg = 'watch_id'
#     permission_classes = [IsAuthenticated, IsWatchOwner]
#     serializer_class = WatchUpdateSerializer


class UpdateWatch(APIView):
    permission_classes = [IsAuthenticated, IsWatchOwner]
    
    def put(self, request, watch_id, *args, **kwargs):
        watch = Watch.objects.get(id=watch_id)
        watch.availability = not watch.availability
        watch.save()
        return Response(WatchUpdateSerializer(watch).data)



class DeleteWatch(DestroyAPIView):
    queryset = Watch.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'watch_id'
    permission_classes = [IsAuthenticated, IsWatchOwner]

class CreateWatch(CreateAPIView):
    serializer_class = CreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
            serializer.save(user=self.request.user)


#Cart CUD
class CartList(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['watch']

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CreateCart(APIView):

    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    # def get_queryset(self):
    #     queryset= Watch.objects.all()
    #     watch_id=self.kwargs.get('watch_id', None)
    #     if watch_id is not None:
    #         queryset= queryset.filter(id=watch_id)
    #     return watch

    
    ##delete watch
    ##user history

    def post(self, request, *args, **kwargs):
        watch = Watch.objects.get(id=kwargs.get('watch_id'))

        if (self.request.user.carts.filter(status=False)):
            cart = Cart.objects.get(user=self.request.user, status= False)
            if not cart.watches.get(id=watch.id):
                cart.watches.add(watch)
                cart.save()
        else:
            cart = Cart(user=self.request.user)
            cart.save()
            cart.watches.add(watch)
            cart.save()
        response = CartSerializer(cart).data
        response['watch'] = WatchListSerializer(watch).data
        return Response(response)

class Checkout (APIView):
    serializer_class= CartListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        cart = Cart.objects.get(user=self.request.user, status=False)
        serializer = CheckoutSerializer(cart)
        for watch in cart.watches.all():
                watch.availability = False
                watch.user=self.request.user
                watch.save()
        cart.status=True
        cart.save()
        return Response(serializer.data)


        


class CartUpdate(RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'cart_id'
    permission_classes = [IsAuthenticated]

class CartHistory(ListAPIView):
    serializer_class = CartSerializer
    def get_queryset(self):
       return Cart.objects.filter(user=self.request.user, status=True)


class CartItemDelete(DestroyAPIView):
    queryset = Watch.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'cart_id'
    permission_classes = [IsAuthenticated, IsWatchOwner]

    def delete(self, request, *args, **kwargs):
        watch = self.get_object()
        cart = Cart.objects.filter(user=self.request.user, status=True)
        cart[0].watches.remove(watch)
        return Response({"status" : 200})

# class CheckOut()

# class DeleteWatch(DestroyAPIView):
#   queryset = Watch.objects.all()
#   lookup_field = 'id'
#   lookup_url_kwarg = 'watch_id'
#   permission_classes = [IsAuthenticated]

# class CreateAddressAPIView(CreateAPIView):
#   serializer_class = AddressSerializer

# class EditAddressAPIView(RetrieveUpdateAPIView):
#   queryset = Address.objects.all()
#   serializer_class = AddressSerializer
#   lookup_field = 'id'
#   lookup_url_kwarg = 'address_id'

# class DestroyAddressAPIView(DestroyAPIView):
#   queryset = Address.objects.all()
#   serializer_class = AddressSerializer
#   lookup_field = 'id'
#   lookup_url_kwarg = 'address_id' 