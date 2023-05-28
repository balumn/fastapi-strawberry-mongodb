import strawberry


@strawberry.type
class User:
    name: str
    photo_url: str
    email_id: str
    mobile: str
    created_on: str
    updated_on: str


@strawberry.type
class FullUser(User):
    _id: str


def user_to_dict(user: User):
    return {
        "name": user.name,
        "photo_url": user.photo_url,
        "email_id": user.email_id,
        "mobile": user.mobile,
        "created_on": user.created_on,
        "updated_on": user.updated_on
    }


def user_from_dict(dict_data: dict):
    return FullUser(
        _id=dict_data.get("_id"),
        name=dict_data.get("name"),
        photo_url=dict_data.get("photo_url"),
        email_id=dict_data.get("email_id"),
        mobile=dict_data.get("mobile"),
        created_on=dict_data.get("created_on"),
        updated_on=dict_data.get("updated_on"),
    )
