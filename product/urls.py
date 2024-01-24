from django.urls import path
from .import views

urlpatterns = [
    path('details/<int:id>',views.DetailsPostView.as_view(), name='details'),
    path('purchase/<int:id>/', views.PurchaseView.as_view(), name='purchase_product'),
    path('wishlist/<int:id>/', views.WishlistView.as_view(), name='wishlist_product'),
]