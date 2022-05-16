from logging import exception
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import hostelsportsequipment
from .serializers import hostelsportsequipmentSerializer


@api_view(['GET'])
def myapp(request):
    hostelsportsequipment1=hostelsportsequipment.objects.all()
    serializer=hostelsportsequipmentSerializer(hostelsportsequipment1, many=True)
    return Response({'status':200,'payload':serializer.data})

@api_view(['POST'])
def post_equipm(request):
    serializer=hostelsportsequipmentSerializer(data=request.data)

    if not serializer.is_valid():
        print (serializer.errors)
        return Response({'status':403,'errors':serializer.errors,'message':'something is wrong'})

    serializer.save()
    return Response({'status':200,'payload':serializer.data})

    
@api_view(['PUT'])
def update_equipm(request,id):
    try:
        hostelsportsequipment2=hostelsportsequipment.objects.get(id=id)
        serializer=hostelsportsequipmentSerializer(hostelsportsequipment2, data=request.data)

        if not serializer.is_valid():
            print (serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':'something is wrong'})

        serializer.save()
        return Response({'status':200,'payload':serializer.data})
    except Exception as e:
        return Response({'status':403, 'message':'invalid id'})

