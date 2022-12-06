import pytest
from rest_framework import status
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_register_user():
    payload = {
        "email": "john.dee@com.pl",
        "first_name": "John",
        "last_name": "Dee",
        "password": "secretpassword",
    }

    response = client.post("/v1/api/auth/register/", data=payload)
    assert response.status_code == status.HTTP_201_CREATED
