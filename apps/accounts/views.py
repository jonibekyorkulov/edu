from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import LoginSerializer, LogoutSerializer, AccessRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework.views import APIView





# Create your views here.
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = LogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        try:
            refresh_token = self.request.data['refresh']
            token = RefreshToken(refresh_token)
            
            token.blacklist()
            logout(self.request)
            data = {
                "status" : True,
                "token" : str(token),
                "message" : "successfully logged out"
            }
            return Response(data, status=205)
        except Exception as e:
            data = {
                'status' : False,
                "message" : 'you are not logged in yet bro'
            }
            return Response(data, status=400)
        
class AccessRefreshView(TokenRefreshView):
    serializer_class = AccessRefreshSerializer