from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import requests

from .serializers import AdhaarAuthSerializer

class AdhaarAuthView(APIView):
    def post(self, request):
        serializer = AdhaarAuthSerializer(data=request.data)
        if serializer.is_valid():
            adhaar_number = serializer.validated_data['adhaar_number']
            payload = {'adhaar_num': adhaar_number, 'x-client-id': None}
            url = 'https://api.cashfree.com/verification/adhaar/'
            headers = {
                'accept': 'application/json',
                'content-type': 'application/json'
            }
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                return Response({"message": "Adhaar verified Successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Adhaar verification failed'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)