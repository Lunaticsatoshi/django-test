from django.shortcuts import render
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes

from .schema import pricing_schema
from .models import Pricing
from .utils import calculate_price

# Create your views here.
@swagger_auto_schema(method='post', request_body=pricing_schema)
@api_view(['POST'])
def get_price(request):
                                        
    """
    @desc     Get price via api
    @route    GET /api/v1/price/
    @access   Public
    @return   Json
    """
    data = request.data
    distance_traveled = data.get('distance')
    time_traveled = data.get('time')
    
    try:
        pricing_config = Pricing.objects.filter(status='Active').latest('updated_at')
        total_price = calculate_price(time_traveled, distance_traveled, pricing_config)
        return Response({'messsage': 'Success', 'data': total_price}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({'message': 'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
