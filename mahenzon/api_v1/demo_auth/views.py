import secrets
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Header
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
    "john": "password",
}

static_auth_token_to_username = {
    "6759bf613a36cb2a33a33534c888c569": "admin",
    "a3d570d7096c164a5b8f370673ad1893": "john",
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


def get_username_by_static_auth_token(
    static_token: str = Header(alias="x-auth-token"),
) -> str:
    if username := static_auth_token_to_username.get(static_token):
        return username
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
    )


@router.get("/basic-auth-username/")
def demo_basic_auth_username(
    auth_username: str = Depends(get_auth_user_username),
):
    return {
        "message": f"Hi, {auth_username}",
        "username": auth_username,
    }


@router.get("/some-http-header-auth/")
def demo_auth_some_http_header(
    username: str = Depends(get_username_by_static_auth_token),
):
    return {
        "message": f"Hi, {username}",
        "username": username,
    }
