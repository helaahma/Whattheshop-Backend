from django.urls import path
from .views import (ProfileUpdate,UserCreateAPIView,WatchList,WatchDetail,UpdateWatch,DeleteWatch,CreateWatch,CartUpdate,CreateCart,CartList)
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', WatchList.as_view(), name='list'),
    path('detail/<int:watch_id>/',WatchDetail.as_view(), name='detail' ),
    path('create/',CreateWatch.as_view(), name='create' ),
    path('list/cart/', CartList.as_view(), name='list-cart'),
    path('update/cart/<int:watch_id>/', CartUpdate.as_view(),name='update-cart'),
    path('create/cart/', CreateCart.as_view(),name='create-cart'),
    path('update/<int:watch_id>/',UpdateWatch.as_view(), name='update' ),
    path('delete/<int:watch_id>/',DeleteWatch.as_view(), name='delete' ),
    path('profile-update/<int:profile_id>/',ProfileUpdate.as_view(), name='profile_update' ),

]