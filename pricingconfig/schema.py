from drf_yasg import openapi

pricing_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'distance': openapi.Schema(type=openapi.TYPE_INTEGER, description='string'),
        'time': openapi.Schema(type=openapi.TYPE_INTEGER, description='string'),
    },
    required=['distance', 'time']
)