from rest_framework import serializers
from .models import Category, Product, Offer, CartItem, User, Checkout,AdminContact


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Product
        fields = ('id', 'p_name', 'description', 'price', 'cat','image')


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'code', 'description', 'discount_percent', 'p')



class CartSerializer(serializers.ModelSerializer):
    # cart_items = CartItemSerializer(many=True)

    class Meta:
        model = CartItem
        fields = ('id', 'Prod_name', 'quantity')






class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'], validated_data['email'], validated_data['password'])

        return user


class CheckoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Checkout
        fields = ["pname"]
    def __str__(self):
        return self.pname
      


class AdminContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminContact
        fields = '__all__'    


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
        fields = ('id', 'username', 'email')