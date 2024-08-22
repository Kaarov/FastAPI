import secrets
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter(
    prefix="/demo_auth",
    tags=["Demo Auth"],
)

security = HTTPBasic()


@router.get("/basic-auth/")
def demo_basic_auth_credentials(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return {
        "message": "Basic Auth Example",
        "username": credentials.username,
        "password": credentials.password,
    }


username_to_password = {
    "admin": "admin",
    "john": "qwerty",
}


def get_auth_user_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )
    correct_password = username_to_password.get(credentials.username)
    if credentials.username not in username_to_password:
        raise unauthed_exc

    # secrets
    if not secrets.compare_digest(
        credentials.password.encode("utf-8"),
        correct_password.encode("utf-8"),
    ):
        raise unauthed_exc

    return credentials.username


@router.get("/basic-auth-username/")
def demo_basic_auth_username(
    auth_username: str = Depends(get_auth_user_username),
):
    return {
        "message": f"Hi, {auth_username}",
        "username": auth_username,
    }
