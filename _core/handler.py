from rest_framework.views import exception_handler
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError, ParseError
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    if isinstance(exc, ObjectDoesNotExist):
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    if isinstance(exc, (ValidationError, ParseError)):
        return Response(exc.detail, status=exc.status_code)

    return exception_handler(exc, context)
