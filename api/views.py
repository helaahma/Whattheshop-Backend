from rest_framework.generics import (ListAPIView, RetrieveAPIView,CreateAPIView, DestroyAPIView)
from .serializers import (UserCreateSerializer, WatchListSerializer, WatchDetailSerializer, ProfileSerializer,)
from rest_framework.filters import (SearchFilter, OrderingFilter,)
from .models import (Brand, Watch,Profile,)
from .permissions import IsWatchOwner



class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

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

class DeleteWatch(DestroyAPIView):
	queryset = Watch.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'watch_id'
	permission_classes = [IsAuthenticated, IsBookingOwner]

class CreateWatch(CreateAPIView):
	serializer_class = WatchDetailSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)









