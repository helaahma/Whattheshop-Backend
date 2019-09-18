from rest_framework.generics import (RetrieveUpdateAPIView,ListAPIView, RetrieveAPIView,CreateAPIView, DestroyAPIView)
from .serializers import (CartSerializer, UserCreateSerializer, WatchListSerializer, WatchDetailSerializer, ProfileSerializer,)
from rest_framework.filters import (SearchFilter, OrderingFilter,)
from .models import (Brand, Watch,Profile, Cart)
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
	serializer_class = WatchDetailSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self,serializer):
			serializer.save(user=self.request.user)

#Cart CUD
class CartList(ListAPIView):
	queryset = Cart.objects.all()
	serializer_class = CartSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['watch']


class CreateCart(CreateAPIView):
	serializer_class = CartSerializer
	permission_classes = [IsAuthenticated]

class CartUpdate(RetrieveUpdateAPIView):
	queryset = Watch.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'watch_id'
	permission_classes = [IsAuthenticated]
	def get_serializer_class(self,request):
		if !self.request.Cart.status:
			return serializer_class = CheckoutSerializer
		else:
			return serializer_class = CartSerializer

class DeleteWatch(DestroyAPIView):
	queryset = Watch.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'watch_id'
	permission_classes = [IsAuthenticated]









