from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def multiply(request):
    try:
        first_param = float(request.query_params.get('first', 0))
        second_param = float(request.query_params.get('second', 0))
        result = first_param * second_param
        return Response(
            {'result': result}
        )
    except ValueError:
        return Response({
            'status': 'error',
            'error': 'Invalid input'
        },
            status=status.HTTP_400_BAD_REQUEST)
