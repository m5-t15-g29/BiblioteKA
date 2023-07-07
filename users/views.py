from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, SendEmailSerializer
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwnerOrIsSuperuser
from rest_framework.views import APIView, Response, Request
from django.core.mail import send_mail
from django.conf import settings


class UserView(CreateAPIView):
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrIsSuperuser]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class SendEmailView(APIView):
    def post(self, req: Request) -> Response:
        serializer = SendEmailSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        send_mail(
            **serializer.validated_data,
            from_email=settings.EMAIL_HOST_USER,
            fail_silently=False
        )

        return Response({"message": "E-mails has been sent"})
