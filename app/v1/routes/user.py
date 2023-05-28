from datetime import datetime
from typing import List
import strawberry

from app.core.schemas.user import User
from app.v1.services.user import get_all_users_from_mongo, insert_user_to_mongo


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello, Dobby here! Where do you wanna go ?"

    @strawberry.field
    def all_users(self) -> List[User]:
        return get_all_users_from_mongo()


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, photo_url: str, email_id: str, mobile: str) -> User:
        user_input = User(
            name=name, photo_url=photo_url, email_id=email_id, mobile=mobile,
            created_on=datetime.now(), updated_on=datetime.now()
        )
        insert_user_to_mongo(user_input)
        return user_input


schema = strawberry.Schema(query=Query, mutation=Mutation)
