from msrj.dbPool import session
from goods.models import ProductInfo
import random

for num in range(1,10):
    product1 = ProductInfo(
        code = 'A' + str(num),
        name = '产品' + str(num),
        costPrice = random.random()
    )
    session.add(product1)
session.commit()

# prod1 = session.query(ProductInfo)
prod1 = session.query(ProductInfo).order_by(ProductInfo.create_date)
print(prod1.count())

