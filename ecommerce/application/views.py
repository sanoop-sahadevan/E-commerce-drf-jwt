

from django.core.mail import send_mail


from rest_framework import filters

# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import generics, permissions
from .models import Category, Product, Offer, CartItem, AdminContact
from .serializers import CategorySerializer, ProductSerializer, OfferSerializer, RegisterSerializer, CheckoutSerializer, CartSerializer, AdminContactSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.response import Response


class Categorycreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Productcreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(generics.ListAPIView):

    serializer_class = ProductSerializer

    def get_queryset(self):
        query_set = Product.objects.all()
        if "search" in self.request.GET:
            search = self.request.GET.get("search")
            query_set = query_set.filter(p_name__icontains=search)
        if "ordering" in self.request.GET:
            ordering = self.request.GET.get("ordering")
            query_set = query_set.order_by(ordering)
        return query_set


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'pk'


class ProductOffercreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class Productofferlist(generics.ListAPIView):

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class ProductsDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAdminUser)


class AddToCart(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer

    def post(self, request, id):
        Prod_name = Product.objects.get(pk=id)
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            quantity = serializer.validated_data['quantity']
            # Check if item is already in the cart
            try:
                cart_item = CartItem.objects.get(Prod_name=Prod_name)
                cart_item.quantity += quantity
                cart_item.save()
            except CartItem.DoesNotExist:
                # Add item to cart
                cart_item = CartItem(Prod_name=Prod_name, quantity=quantity)
                cart_item.quantity = quantity
                cart_item.save()
            # return Response(status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        response_data = {
            "message": "User created successfully",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }
        return Response(response_data)


class CheckoutView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CheckoutSerializer

    def perform_create(self, request):
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        pname = serializer.data["pname"]

        user_email = self.request.user.email
        subject = 'Thank you for your purchase'
        message = 'Dear {},\n\nThank you for your purchase. Your order for {} has been successfully processed.'.format(
            self.request.user.username, pname)
        from_email = 'sanoopsahadevan99@gmail.com'
        recipient_list = [user_email]
        send_mail(subject, message, from_email,
                  recipient_list, fail_silently=True)
        return Response("pname")


class AdminContactCreateAPIView(generics.CreateAPIView):
    queryset = AdminContact.objects.all()
    serializer_class = AdminContactSerializer
    permission_classes = [IsAdminUser]


class AdmincontactlistView(generics.ListAPIView):
    queryset = AdminContact.objects.all()
    serializer_class = AdminContactSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
