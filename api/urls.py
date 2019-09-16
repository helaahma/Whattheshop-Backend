from django.urls import path
from .views import (UserCreateAPIView,WatchList,WatchDetail,UpdateWatch,DeleteWatch,CreateWatch)
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', WatchList.as_view(), name='list'),
    path('detail/<int:watch_id>/',WatchDetail.as_view(), name='detail' ),
    path('create/',CreateWatch.as_view(), name='create' ),
    path('detail/<int:watch_id>/',UpdateWatch.as_view(), name='update' ),
    path('detail/<int:watch_id>/',DeleteWatch.as_view(), name='delete' ),
]