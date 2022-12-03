from http import HTTPStatus
from typing import Mapping, Optional

from rest_framework.response import Response as RestResponse


class Response(RestResponse):
    def __init__(
        self,
        data: Optional[Mapping] = None,
        status: HTTPStatus = HTTPStatus.OK,
        headers: Optional[Mapping] = None,
        content_type: Optional[str] = None,
    ):
        super().__init__(
            data=data,
            status=status,
            template_name=None,
            headers=headers,
            exception=None,
            content_type=content_type,
        )


class ErrorResponse(Response):
    _FIELD_ERROR = "detail"

    def __init__(self, message: Optional[str], status: HTTPStatus):
        super().__init__(data={self._FIELD_ERROR: message}, status=status)
