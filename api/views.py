from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Product, BasketItem
from .serializers import ProductSerializer, BasketItemSerializer
from django.core.mail import send_mail

# Create your views here.


@api_view(['GET'])
def getAllProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createBasketItem(request):
    data = request.data
    selected_product = Product.objects.get(name=data['product_name'])
    if selected_product.inventory >= int(data['quantity']):
        selected_product.inventory -= int(data['quantity'])
        selected_product.save()
        basket_item = BasketItem.objects.create(
            product_name=data['product_name'],
            quantity=data['quantity']
        )
        return Response({'hold_id': basket_item.id})
    else:
        return Response({'message': 'Stoc insuficient'})


@api_view(['DELETE'])
def removeBasketItem(request, pk):
    basket_item = BasketItem.objects.get(id=pk)
    product = Product.objects.get(name=basket_item.product_name)
    product.inventory += basket_item.quantity
    product.save()
    basket_item.delete()
    return Response({'message': 'Basket item deleted, inventory restored'})


@api_view(['GET'])
def getBasketItems(request):
    basket_item_ids = request.GET.getlist('basketItems')
    basket_ids = basket_item_ids[0].split(',')
    items = BasketItem.objects.filter(id__in=basket_ids)
    serializer = BasketItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def buyBasket(request):
    print(request.data)
    data = request.data
    message = f'Avem o comanda noua inregistrata de catre: \n' \
              f'Nume: {data["name"]} \n' \
              f'Email: {data["email"]} \n' \
              f'Telefon: {data["phone"]} \n' \
              f'Mesaj: {data["message"]} \n' \

    basket_item_ids = request.GET.getlist('basketItems')
    basket_ids = basket_item_ids[0].split(',')
    basket_items = BasketItem.objects.filter(id__in=basket_ids)
    for item in basket_items:
        message += f'{item.product_name}  |  {item.quantity} \n'
        item.delete()

    subject = 'Comanda Plasata'
    from_email = 'miklos_steel23@gmail.com'
    recipient_list = ['stefan.curcubet@gmail.com']
    send_mail(subject, message, from_email, recipient_list)
    return Response({'message': 'Basket bought, email sent'})

