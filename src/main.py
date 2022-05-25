import asyncio

import graphene
from graphene import ObjectType, Field, Int, List

from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp, make_playground_handler
from src.schemas.schema import ProductOverview, ProductType
import json


class Query(ObjectType):
    product_overview = Field(ProductOverview)
    product_details = Field(ProductType, id=Int())
    products_by_category = List(ProductType, categoryId=Int())

    @staticmethod
    async def resolve_product_overview(self, info):
        with open("src/products.json") as products_json:
            products = json.load(products_json)
        return {
                    'products': products,
                    'totalProducts':  len(products),
                    'totalPrice': (sum(d.get('price', 0) for d in products)),
        }

    @staticmethod
    async def resolve_product_details(self, info, id):
        with open("src/products.json") as products:
            products = json.load(products)
        product = next((product for product in products if product['id'] == id), None)
        return product

    @staticmethod
    async def resolve_products_by_category(self, info, categoryId):
        with open("src/products.json") as products_json:
            products = json.load(products_json)
        products = [product for product in products if product['category'] == categoryId]
        return products


class Subscription(graphene.ObjectType):
    count = graphene.Int(upto=graphene.Int())

    async def subscribe_count(root, info, upto=3):
        for i in range(upto):
            yield i
            await asyncio.sleep(1)


app = Starlette()
schema = graphene.Schema(query=Query, subscription=Subscription)

app.mount("/", GraphQLApp(schema, on_get=make_playground_handler()))  # Playground IDE
