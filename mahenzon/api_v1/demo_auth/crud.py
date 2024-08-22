from auth import utils as auth_utils
from users.schemas import UserSchema


john = UserSchema(
    username="john",
    password=auth_utils.hash_password("qwerty"),
    email="john@gmail.com",
)
sam = UserSchema(
    username="sam",
    password=auth_utils.hash_password("secret"),
)

user_db: dict[str, UserSchema] = {
    john.username: john,
    sam.username: sam,
}
