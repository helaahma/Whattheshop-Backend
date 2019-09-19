from rest_framework.generics import (RetrieveUpdateAPIView,ListAPIView, RetrieveAPIView,CreateAPIView, DestroyAPIView)
from .serializers import (CreateSerializer,CheckoutSerializer,CartSerializer, UserCreateSerializer, WatchListSerializer, CartListSerializer, WatchDetailSerializer, ProfileSerializer,)
from rest_framework.filters import (SearchFilter, OrderingFilter,)
from .models import ( Watch,Profile, Cart)
from .permissions import IsWatchOwner
from rest_framework.permissions import IsAuthenticated



class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ProfileUpdate(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'

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

class UpdateWatch(RetrieveUpdateAPIView):
    queryset = Watch.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'watch_id'
    permission_classes = [IsAuthenticated, IsWatchOwner]
    serializer_class = WatchDetailSerializer

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


class CreateCart(CreateAPIView):

    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
        watch = Watch.objects.get(id=self.kwargs['watch_id'])
        cart = Cart(user=self.user)
        cart.save()
        cart.watches.add(watch)
        cart.save()
        return cart


class CartUpdate(RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'cart_id'
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if (self.get_object().status==False):
            for watch in self.get_object().watches.all():
                watch.availability = False
                watch.save()
            return CheckoutSerializer
        else:
            return CartSerializer

    def perform_update(self, serializer):
        serializer.save(status=False)


# class CheckOut()

# class DeleteWatch(DestroyAPIView):
#   queryset = Watch.objects.all()
#   lookup_field = 'id'
#   lookup_url_kwarg = 'watch_id'
#   permission_classes = [IsAuthenticated]









