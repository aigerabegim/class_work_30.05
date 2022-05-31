from urllib import response
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.account import serializers

from .models import ShoppingCart, CartItem
from .serializers import CartItemSerializers, CartSerializer


class ShoppingCartView(APIView):

    def get(self, request):
        user = request.user
        cart = user.cart
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def put(self, request, pk=None):
        cart = request.user.cart
        try:
            cart_item: CartItem = cart.cart_item.get(pk=pk)
        except CartItem.DoesNotExist:
            return Response({'message': 'no object was found'}, status=status.HTTP_204_NO_CONTENT)

        quantity = request.data.get('quantity')
        cart_item.quantity = int(quantity)
        cart_item.save()
        serializer = CartItemSerializers(cart_item)
        return Response(serializer.data)

    def delete(self, request, pk):
        cart = request.user.cart
        try:
            cart_item: CartItem = cart.cart_item.get(pk=pk)
        except CartItem.DoesNotExist:
            return Response({'message': 'no object was found'}, status=status.HTTP_204_NO_CONTENT)

        cart_item.delete()
        return Response(status=status.HTTP_200_OK)


class AddProductInCartView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.POST
        serializer = CartItemSerializers(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


