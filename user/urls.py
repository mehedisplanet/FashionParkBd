
from django.urls import path
from .views import UserLogout,signup,ProfileView,WishlistView,BasketView
from . import views
from .views import  UserLoginView
from .views import activate
 
urlpatterns = [
    path('register/', signup, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogout, name='logout'),
    path('activate/<uidb64>/<token>/',  
        activate, name='activate'),  
    path('profile/', ProfileView.as_view(), name='profile' ),
    path('basket/', BasketView.as_view(), name='basket' ),
    path('wishlist/', WishlistView.as_view(), name='wishlist' ),
]