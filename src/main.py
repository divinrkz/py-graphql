import asyncio

import graphene
from graphene import ObjectType, Field

from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp, make_playground_handler
from src.schemas.schema import ProductOverview
import json


class Query(ObjectType):
    products = None
    product_overview = Field(ProductOverview)

    async def resolve_product_overview(self, info):
        with open("src/products.json") as products:
            products = json.load(products)
        return {'products': products}


class Subscription(graphene.ObjectType):
    count = graphene.Int(upto=graphene.Int())

    async def subscribe_count(root, info, upto=3):
        for i in range(upto):
            yield i
            await asyncio.sleep(1)


app = Starlette()
schema = graphene.Schema(query=Query, subscription=Subscription)

app.mount("/", GraphQLApp(schema, on_get=make_playground_handler()))  # Playground IDE
