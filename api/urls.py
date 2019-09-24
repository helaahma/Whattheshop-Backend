from django.urls import path
from .views import (CartItemDelete,CartHistory,Checkout,ProfileUpdate,ProfileDetail,UserCreateAPIView,
                    WatchList,WatchDetail,UpdateWatch,DeleteWatch,CreateWatch,
                    CartUpdate,CreateCart,CartList, CreateAddressAPIView, EditAddressAPIView, DestroyAddressAPIView)
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', WatchList.as_view(), name='list'),
    path('detail/<int:watch_id>/',WatchDetail.as_view(), name='detail' ),
    path('create/',CreateWatch.as_view(), name='create' ),
    path('list/cart/', CartList.as_view(), name='list-cart'),
    path('update/cart/<int:cart_id>/', CartUpdate.as_view(),name='update-cart'),
    path('create/cart/<int:watch_id>/', CreateCart.as_view(),name='create-cart'),
    path('delete/cart/<int:cart_id>/', CartItemDelete.as_view(),name='delete-cart'),
    path('checkout/', Checkout.as_view(),name='checkout'),
    path('history/', CartHistory.as_view(), name = 'history'),
    path('update/<int:watch_id>/',UpdateWatch.as_view(), name='update' ),
    path('delete/<int:watch_id>/',DeleteWatch.as_view(), name='delete' ),
    path('profile/update/<int:profile_id>/',ProfileUpdate.as_view(), name='profile_update' ),
    path('profile/detail/<int:profile_id>/',ProfileDetail.as_view(), name='profile_detail' ),
    path('address/create/',CreateAddressAPIView.as_view(), name = 'address-create' ),
    path('address/<int:address_id>/edit/',EditAddressAPIView.as_view(), name = 'address-edit' ),
    path('address/<int:address_id>/delete/',DestroyAddressAPIView.as_view(), name = 'address-delete' ),

]