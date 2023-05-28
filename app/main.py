import strawberry
from strawberry.tools import create_type
from strawberry.fastapi import GraphQLRouter

from fastapi import FastAPI

from os import getenv

from app.v1.routes.user import schema as user_schema

# # override PyObjectId and Context scalars
# from .models import PyObjectId
# from .otypes import Context, PyObjectIdType


# # create query types
# Query = create_type("Query", [get_user])
#
# # create mutation types
# Mutation = create_type("Mutation", [create_user])
#
#
# # initialize federated schema
# schema = strawberry.Schema(
#     query=Query,
#     mutation=Mutation
# )

# Get env variable of whether to run application in Debug Mode
DEBUG = getenv("TEMPLATE_DEBUG", "false").lower() in ("true", "1", "t")

# serve API with FastAPI router
user_app = GraphQLRouter(user_schema)
app = FastAPI(
    debug=DEBUG,
    title="Dobby Travels",
    desciption="Integration of FastAPI and Strawberry with Mongodb",
    port=5000
    )
app.include_router(user_app, prefix="/graphql")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health():
    return {"status": "OK"}
