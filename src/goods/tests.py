from msrj.dbPool import session
from goods.models import ProductInfo
import random

product1 = ProductInfo(
    code = 'A' + str(random.randint(100,200)),
    name = '产品一',
    costPrice = random.random()
)

session.add(product1)
session.commit()

# prod1 = session.query(ProductInfo)
prod1 = session.query(ProductInfo).order_by(ProductInfo.create_date)
print(prod1.count())

