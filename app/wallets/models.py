from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Wallets(Base):
    __tablename__ = 'wallet'

    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: Mapped[int]
    amount: Mapped[int]
