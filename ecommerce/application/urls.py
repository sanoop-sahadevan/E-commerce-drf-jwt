
from django.urls import path
from .views import CategoryList, Categorycreate, ProductList, Productcreate, ProductOffercreate, Productofferlist, AddToCart, RegisterAPIView, CheckoutView, AdminContactCreateAPIView, AdmincontactlistView, ProductsDeleteView, ProductDetailView, UserProfileView

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path("catcreate/", Categorycreate.as_view(), name="cat-create"),
    path('productlist/', ProductList.as_view(), name='product-list'),
    path('productscreate/', Productcreate.as_view(), name='product-create'),
    path('products/offercreate/', ProductOffercreate.as_view(),
         name='product-offer-create'),
    path('products/offerlist/<int:pk>',
         Productofferlist.as_view(), name='product-offer-list'),
    path('productsdelete/<int:pk>/', ProductsDeleteView.as_view()),
    path('productsdetail/<int:pk>/',
         ProductDetailView.as_view(), name='product_detail'),
    path('cart/add/<int:id>', AddToCart.as_view(), name='cart-add-item'),
    
   



    path('admin-contact/', AdminContactCreateAPIView.as_view(),
         name='admin-contact-create'),
    path('admin-contactlist/', AdmincontactlistView.as_view(),
         name='admin-contact-list'),



    path('register/', RegisterAPIView.as_view(), name='register'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),


]
