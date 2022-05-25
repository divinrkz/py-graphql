from graphene import ID, ObjectType, String, Schema, Int, List


class ProductType(ObjectType):
    id = ID()
    name = String()
    price = Int()
    category = Int()


class ProductOverview(ObjectType):
    products = List(ProductType)
    totalProducts = Int()
    totalPrice = Int()




