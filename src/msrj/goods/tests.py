from msrj.dbPool import session
from msrj.goods.models import Game


game1 = Game(
    # company=nintendo,
    category="ACT",
    name="Super Mario Bros",
    release_date='1985-10-18'
)

# session.add(game1)
# session.commit()


qrys = session.query(Game).filter_by(category="ACT")

print(qrys.count())