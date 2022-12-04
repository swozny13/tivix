from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from common.http.response import ErrorResponse
from user.api.serializers import RegisterSerializer, UserDetailSerializer
from user.api.validators import CreateUserValidator
from user.domain.command.create_user import create_user_command
from user.domain.query.user_by_id import get_user_by_id
from user.exceptions import UserAlreadyExistsException
from user.mappers import UserCreateDTOMapper


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        validator = CreateUserValidator(data=request.data)

        if not validator.is_valid():
            return Response(data=validator.errors, status=status.HTTP_400_BAD_REQUEST)

        user_data = UserCreateDTOMapper.from_json(json=validator.validated_data)

        try:
            user = create_user_command.execute(user_data)
        except UserAlreadyExistsException as e:
            return ErrorResponse(status=status.HTTP_409_CONFLICT, message=str(e))

        serializer = RegisterSerializer(user)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class UserDetailView(APIView):
    def get(self, request: Request) -> Response:
        user = get_user_by_id.execute(user_id=request.user.id)
        serializer = UserDetailSerializer(user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
