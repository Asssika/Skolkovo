# Data Access Object
from app.wallets.models import Wallets
from app.dao.base import BaseDAO


class WalletsDAO(BaseDAO):
    model = Wallets
