from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
import jwt, datetime
from django.utils import timezone
from django.contrib.auth import authenticate

class LoginView(APIView):
    permission_class = (AllowAny,)
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            payload = {
                'id': user.id,
                'exp': timezone.now() + datetime.timedelta(minutes=10),
                'iat': timezone.now()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')

            response = Response()
            
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {'jwt': token}

            return response
        else:
            raise Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Session expired, please login again')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logout successfully'
        }
        return response

