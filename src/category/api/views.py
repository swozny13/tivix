from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from category.api.serializers import CategorySerializer
from category.api.validators import CreateCategoryValidator
from category.domain.commands.create_category import create_category_command
from category.exceptions import CategoryAlreadyExistsException
from category.mappers import CategoryCreateDTOMapper
from common.http.response import ErrorResponse


class CreateCategoryView(APIView):
    def post(self, request: Request) -> Response:

        validator = CreateCategoryValidator(data=request.data)

        if not validator.is_valid():
            return Response(data=validator.errors, status=status.HTTP_400_BAD_REQUEST)

        category_data = CategoryCreateDTOMapper.from_json(json=validator.validated_data)

        try:
            category = create_category_command.execute(category_data)
        except CategoryAlreadyExistsException as e:
            return ErrorResponse(status=status.HTTP_409_CONFLICT, message=str(e))

        serializer = CategorySerializer(category)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
